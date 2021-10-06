from numpy import *
from idlsave import read
from functools import reduce
from itertools import accumulate
from os.path import expanduser
from os.path import dirname, join
import pickle

_is_pycuda = True
_is_KSTARonline = True

qe = 1.6021892E-19
me = 9.109534E-31
c = 0.29979246      #Speed of light (10^9 m/s)
rin = 1.26      #Distance to the tile surface (m)
s_omega0 = 6.0
epsi=8.8541878E-12   #Electric permittivity
p = (1.6021892E-19)**2/(8.8541878E-12 * 9.109534E-31) #  %p * n_el = omega_pe^2 (3182.6)
pp=p/(2.*pi)**2           #n_e=frequency^2/pp
Rmajor = 1.8 #Major radius
ce = qe/2/pi/me
dt_sweep = 20. #20 us 

try:
    from gpreflkernel import  gpCwtMorlet, gpRecoverDPhase, gpGetCutoff, gpCalcDensity, gpGetPeaktrace, gpadd_refph0
except:
    _is_pycuda = False
    
def _CwtMorlet ( l_data, l_scale):
    # Morlet wavelet function
    def Morlet_wf( s_omega, s_omega0):
        H = ones(len(s_omega))
        n = len(s_omega)
        for i in range(len(s_omega)):
            if s_omega[i] < 0.0: H[i]=0.0
            # !!!! note : was s_omega/8 before 17/6/03
        xhat=0.75112554*( exp(-(s_omega-s_omega0)**2/2.0))*H
        return xhat
    #
    l_CWT = []
    for iband, data in enumerate(l_data):
        scale = l_scale[iband]
        nscale = scale.size
        nsig = data.shape[0]
        ndata = data.shape[1]              
        datahat= fft.fft(data)
        CWT = zeros( (nsig*nscale, ndata), complex64)
        omega= array([*range(0,ndata//2)]+[*range(-ndata//2,0)])*(2.0*pi/ndata)
        #omega= array(range(0,Ndata/2+1))*(2.0*pi/Ndata)
        for ii, sc in enumerate(scale):
            s_omega = sc*omega
            psihat= sqrt(2.0*pi*sc)*Morlet_wf(s_omega, s_omega0)
            jidx_list = map(lambda j: nscale*j+ii, range(nsig))
            convhat = psihat * datahat
            W = fft.ifft(convhat)
            CWT[[*jidx_list],:] = W
        l_CWT.append(CWT.reshape((nsig,nscale,ndata)))
    return l_CWT


def _RecoverDPhase(l_CWT, l_scale, l_iwindow, ph0ref, nhead, bandstr):
    l_dphase = []
    l_ipeak = []
    l_istop = []
    for iband, band in enumerate(bandstr):
        iwindow = l_iwindow[iband]
        scale = l_scale[iband]
        if len(iwindow) != 3 :
            raise Exception("Error in input format (window must have 3 lists)")
        elif len(iwindow[0]) != len(iwindow[1]) or len(iwindow[1]) != len(iwindow[2]):
            raise Exception("Error in input format (the lists in window must have the same length)")
        nsig = l_CWT[iband].shape[0]            
        ndata = l_CWT[iband].shape[2]
        res_phdiff = [zeros((nsig,1))]
        res_peakpos = []
        ianomjump = []
        for ii, data_idx in enumerate(accumulate(iwindow[0])):
            nstep = iwindow[0][ii]
            iymin = iwindow[1][ii]
            iymax = iwindow[2][ii]
            ix0 = data_idx + nhead[band]
            
            if data_idx <  ndata:
                wws =  l_CWT[iband][:,iymin:iymax+1,ix0-nstep:ix0+1]
            elif data_idx - nstep <  ndata :
                wws =  l_CWT[iband][:,iymin:iymax+1,ix0-nstep:]
            else:
                wws = array([[[]]])    
                
            peakpos = absolute(wws).argmax(axis=1)
            peakval = array([ [wws[ii, jj, kk] for kk, jj in enumerate(js)] for ii, js in enumerate(peakpos)])            
            phasediff = angle(peakval[:,1:]*conjugate(peakval[:,:-1]))
            absdiff = abs(peakpos[: ,1:]-peakpos[:, :-1]) 

            ipkjump = zip(*nonzero( absdiff > 0.0))
            iphjump = zip(*nonzero( phasediff < 0.0))
            for idx in iphjump:
                phasediff[idx] = phasediff[idx] + 2*pi
            for idx in ipkjump:
                p0 = angle(conjugate(wws[idx[0], peakpos[idx], idx[1]])*wws[idx[0], peakpos[idx], idx[1]+1])
                p1 = angle(conjugate(wws[idx[0], peakpos[idx[0], idx[1]+1], idx[1]])*wws[idx[0], peakpos[idx[0], idx[1]+1], idx[1]+1])
                if p0 < 0:
                    p0 = p0 + 2*pi
                if p1< 0:
                    p1= p1+ 2*pi
                phasediff[idx] = .5*(p0+p1)
            res_phdiff.append( phasediff)
            res_peakpos.append( peakpos + iymin)
            ianomjump.append( array(nonzero( absdiff//nstep > 1.0)))
            #res_peakpos.append( peakpos + iymin)            
        
        test_anom = concatenate( ianomjump, axis = 1)
        istop = (ndata-1)*ones( nsig, int)                   
        for i, ii in enumerate(test_anom[0]):
            jj = test_anom[1,i]
            istop[ii] = min(jj, istop[ii])
        dphase = concatenate(res_phdiff, axis = 1)
        n = min(dphase.shape[1], ph0ref[band].size)
        dphase[:,:n]  = dphase[:,:n] - ph0ref[band][:n]
        l_dphase.append( copy(dphase))            
        l_ipeak.append( concatenate(res_peakpos, axis = 1))
        l_istop.append( copy(istop))
    return l_dphase, l_ipeak, l_istop


IDXMIN = 300
MINLEN = 30
def _GetCutoff(dphase, iant):
    dphsub = dphase[:,iant:]
    dphsub[:,IDXMIN] = 0.
    dphsub[:,-1] = 0.
    tmpbools = dphsub[:,IDXMIN:] < 0.
    icut2 = [nonzero( ~b[1:] & b[:-1])[0] for b in tmpbools]
    icut1 = [nonzero( b[1:] & ~b[:-1])[0] for b in tmpbools]    
    cut = array([ ic1[nonzero(icut2[ii] - ic1 > MINLEN)[0][0]]  for ii, ic1 in enumerate(icut1)])
    icut = [ dph[cut[ii]-IDXMIN:cut[ii]].argmax() - IDXMIN + cut[ii] + iant for ii, dph in enumerate(dphsub)]
    return icut


def _SetPhaseData(l_dphase, icut, l_istop, faxis, istart, iend, B0, fSample, bandstr):
    nsig = reduce( min, map(lambda x: x.shape[0], l_dphase))
    frq_data = [array([]) for _ in range(nsig)]
    ph_data = [array([]) for _ in range(nsig)]
    for ii, band in enumerate(bandstr):        
        if ii == 0:
            f_oldend = zeros(nsig)
            ph0 = zeros(nsig)
            idx0 = zeros(nsig, int)
            ioff = icut
            imax = iend[band] + zeros(nsig, int)
        else:
            f_oldend = freq[imax]
            f_newstart = faxis[band][istart[band]]*1e9
            idx0 = imax - ioff - 1 
            ph0 = [(pha[idx0[jj]] - pha[idx0[jj]-1])/(freq[imax[jj]]-freq[imax[jj]-1])*(f_newstart - freq[imax[jj]-1]) + pha[idx0[jj]-1] for jj, pha in enumerate(ph)]
            ioff = istart[band] + zeros(nsig, int)
            if band == bandstr[-1]:
                imax = l_istop[ii]
            else:
                imax = iend[band] + zeros(nsig, int)
        #l_nlen = list(imax + 1 - ioff)
        freq = faxis[band]*1e9
        r0f1e9 = qe/2./pi/me/1E9*B0*Rmajor
        dph0coef = - 4.*pi/c*(faxis[band][-1]-faxis[band][0])/dt_sweep/fSample[band]
        phcorr = dph0coef*(r0f1e9/faxis[bandstr[0]][icut]-rin)
        dphase =  l_dphase[ii] - phcorr.reshape((phcorr.size,1))
        ph = [ cumsum(dph[ioff[jj]:imax[jj]+1])+ ph0[jj] for jj, dph in enumerate(dphase)]
        frq = [ freq[ioff[jj]:imax[jj]+1] for jj in range(nsig)]
        imin = [ nonzero(f_oldend[jj] < fa)[0][0] for jj, fa in enumerate(frq)]
        ph_data = [*map(concatenate, zip(ph_data, [ ph[jj][imin[jj]:] for jj in range(nsig) ]))]
        frq_data = [*map(concatenate, zip(frq_data, [ frq[jj][imin[jj]:] for jj in range(nsig) ]))]    
    return frq_data, ph_data


def _CalcDensity(l_dphase, icut, l_istop, faxis, istart, iend, B0, fSample, bandstr):
    frq_data, ph_data =  _SetPhaseData(l_dphase, icut, l_istop, faxis, istart, iend, B0, fSample, bandstr)
    #
    l_n = []; l_r = []
    nsig = len(frq_data)
    
    for kk in range(nsig):
        phase = ph_data[kk]
        frq = frq_data[kk]
        nlen = phase.size
        nel = zeros(nlen)
        r = zeros(nlen)
        fre_pe = zeros(nlen)
        fre_ce = zeros(nlen)
        r[0] = qe/2/pi/me/frq[0]*B0*1.8
        fre_pe[0] = sqrt(pp*0.0)
        fre_ce[0] = ce*B0*Rmajor/r[0]
        nel[0] = fre_pe[0]**2/pp    
        integ = 0.
        for n in range(1,nlen):    
            freqn2 = frq[n-1]**2
            fre_pen2 = fre_pe[n-1]**2
            fre_cen2 = fre_ce[n-1]**2
            if fre_pen2 < 1e-8:
                myu = 1.
            else:
                myu = 1. - (fre_pen2/freqn2)*(freqn2-fre_pen2)/(freqn2-fre_pen2-fre_cen2)
            delta_r = 1.5/sqrt(myu)*(c*1E9*phase[n-1]/4./pi/frq[n-1] - integ)
            r[n] = r[n-1] - delta_r
            fre_ce[n] = ce*B0*Rmajor/r[n]
            if fre_ce[n] < frq[n-1]:
                fre_pe[n] = sqrt(frq[n-1]**2-frq[n-1]*fre_ce[n])
            else:
                fre_pe[n] = 0.0
            nel[n] = fre_pe[n]**2/pp
            freqn2 = frq[n]**2
            fre_pe2 = fre_pe[:n+1]**2
            fre_ce2 = fre_ce[:n+1]**2
            myuis = sqrt(1.- (fre_pe2/freqn2)*(freqn2-fre_pe2)/(freqn2-fre_pe2-fre_ce2))
            integ = sum(.5*(myuis[1:]+myuis[:-1])*(r[:n]-r[1:n+1]))
        l_r.append(copy(r)) 
        l_n.append(copy(nel))
    return l_r, l_n

                    
class density_profile( object):
    """
    """
    Nqv = 2000; Nw = 4000
    def __init__( self,  shotnumber,  params = "refQVW11383.sav",  withgpu = False):
        self.shot = shotnumber
        self.timestamp = []
        if ( not _is_pycuda): 
            self.withgpu =  False
        else:
            self.withgpu = withgpu
            
        self._ref_bands = ""
        qvwref = read( join(expanduser('.'), "params", params),  verbose=False)
        self._refname = params
        if "pq" in qvwref and "freq" in qvwref:
            ph0q = qvwref["pq"].p[0][:self.Nqv]
            freq = qvwref["freq"][:self.Nqv]
            self._ref_bands = self._ref_bands + "q"
        else:
            ph0q = array([])
            freq = array([])
            
        if "pv" in qvwref and "frev" in qvwref and "isv" in qvwref and ("ioff" in qvwref or "offset" in qvwref):
            ph0v = qvwref["pv"].p[0] [:self.Nqv]
            frev = qvwref["frev"][:self.Nqv]
            isv = qvwref['isv']
            ioff = qvwref['ioff'] if "ioff" in qvwref else qvwref["offset"]
            self._ref_bands = self._ref_bands + "v"
        else:
            ph0v = array([])
            frev = array([])
            isv = -1
            ioff = -1
            
        if "pw" in qvwref and "frew" in qvwref:
            ph0w = qvwref["pw"].p[0] 
            frew = qvwref["frew"]
            isw = qvwref['isw']
            ioffw = qvwref['ioff']
            self._ref_bands = self._ref_bands + "w"
        else:
            ph0w = array([])
            frew = array([])
            isw = -1
            ioffw = -1
            
        nHead = 24
        fSample = 100.0 #MHz
        period = 5000                 
        if frew.size > 3000:
            self.nHead = {'q':nHead, 'v':nHead, 'w':nHead*2}
            self.fSample = {'q':fSample, 'v':fSample, 'w':fSample*2}
            self.period = {'q':period, 'v':period, 'w':period*2}
            isw = isw*2 if isw >= 0 else -1
            ioffw = ioffw*2 if ioffw >= 0 else -1
            ph0w = ph0w[:self.Nw]
            frew = frew[:self.Nw]
        else:
            self.nHead = {'q':nHead, 'v':nHead, 'w':nHead}
            self.fSample = {'q':fSample, 'v':fSample, 'w':fSample}
            self.period = {'q':period, 'v':period, 'w':period}
            ph0w = ph0w[:self.Nqv]
            frew = frew[:self.Nqv]
        #ieq = qvwref['ieq']
        if "v" in self._ref_bands:
            l_tmp = nonzero( freq >= frev[isv])[0]
            ieq = l_tmp[0] if l_tmp != [] else freq.size-1
        else:
            ieq = freq.size-1
        if "w" in self._ref_bands:
            l_tmp = nonzero( frev >= frew[isw])[0]
            iev = l_tmp[0] if l_tmp != [] else frev.size-1
        else:
            iev = frev.size-1
        
        self.istart = {'q':0, 'v':isv, 'w':isw}
        self.iend = {'q':ieq, 'v':iev, 'w':frew.size-1}
        self.ioff = {'q':0, 'v':ioff, 'w':ioffw}
        self.ph0ref = {'q':ph0q, 'v':ph0v, 'w':ph0w}
        self.faxis = {'q':freq, 'v':frev, 'w':frew}
        self.nscale = { 'q':50, 'v':50, 'w':50 }
        self.window = { 'q':array([[]]), 'v':array([[]]), 'w':array([[]])}
        self._sigready = False

    def getTimeInfo( self, band = 'v'):
        time = array([]) 
        nadta = array([]) 
        Ip = array([])
        if _is_KSTARonline:
            with KSTARreflectometer(self.shot) as kstar:
                time, ndata, Ip = kstar.get_timelist(band)
            nseg = array(time).shape[0]
            print("- number of segments =", nseg, "\n")
            print("- time stamps (start and end of the segments):\n", array( [[*map( lambda x : '%.3f' %(x), t)] for t in time]), "\n")
            print("- number of data in the segments:\n", ndata, "\n")
            print("- plasma current of the segments:\n", ["%2.f kA" %(ip/1E3) for ip in Ip], "\n")
        else:
            print("- now off-line..")
        return time, ndata, Ip
        
#    def getTorField( self, t0, t1):
#        B0 = None
#        if _is_KSTARonline:        
#            with KSTARreflectometer( self.shot) as kstar:
#                B0 = kstar.averagetf( t0, t1)
#        else:
#            print("- now off-line..")    
#        return B0

    def getSignal(self, bands = ['v', 'w'], segidx = 0, sigstep = 10):
        self.bands = []
        self.signal = []
        self.timestamp = []
        if _is_KSTARonline:
            bands = [x for x in reduce( lambda x,y:x+y, bands).lower()]
            bands.sort()
            bandstr = reduce( lambda x,y:x+y, bands)
            if bandstr != 'qv' and bandstr != 'vw' and bandstr != 'qvw':  
                raise Exception('Wrong band list')
            self.bands = bands
            with KSTARreflectometer( self.shot) as kstar:
                for ii, band in enumerate(self.bands):
                    print('.. reading time domain information (band = %s) .....' %(band))
                    time, ndata = kstar.get_timeinfo( band, segidx)
                    if ii == 0:
                        B0 = kstar.averagetf( time[0], time[1])
                    if self.bands[0] == 'q' and B0 > 2.25:
                        raise Exception('Check band list : B0 > 2.25 T (%.2f T)' %(B0))
                    print('.. reading rf signal (band = %s, segment index = %d) .....\n' %(band, segidx))
                    if ii == 0:
                        ndx = nonzero( self.faxis[band] > qe/2./pi/me*1E-9*round(B0,1)*1.8/(1.8+0.824))[0]  #frequency greator than cyclotron freq.
                        if ndx == []:
                             raise Exception('Check band list : cannot find the lower limit frequency')
                        else:
                             self.iant = ndx[0]
                    da, i0da = kstar.read_data( band, segidx, ndata)
                    period = self.period[band]
                    nn = period*sigstep
                    ihead_off = self.nHead[band] 
                    itail_off = self.nHead[band] 
                    nlen = da.size - i0da
                    nfaxis = self.faxis[band].size
                    nsig = nlen//nn + 1 if nlen % nn > nfaxis else nlen//nn
                    sig = array([ da[i0da-ihead_off+jj*nn:i0da+itail_off+jj*nn+nfaxis] for jj in range(nsig)])
                    tstamp = array([ (i0da-ihead_off+jj*nn)/self.fSample[band]*1E-6 + time[0] for jj in range(nsig) ])
                    self.signal.append((band, sig))
                    self.timestamp.append((band, tstamp))
                self.signal = dict( self.signal)
                self.timestamp = dict( self.timestamp)
                self.B0 = B0
                self.__set_default_window( B0)
                self._segidx = segidx
                self._sigstep = sigstep
                self._sigready = True
        else:
            self._sigready = False
            print("- now off-line..")                    
        return
    
        
    names = [ "shot",  "_refname", "period", "_segidx", "_sigstep", "bands", "timestamp", "faxis", "signal", "nHead", "iant", "B0", "window"]
    
    def saveSignal(self, fname="reflsig.dat"):
        if self._sigready:
            with open( join(expanduser('.'), 'data', fname), 'wb') as f:                
                 pickle.dump(dict([(idname, getattr(self, idname)) for idname in self.names]), f)
        else:
            print("out of data...")
        return
    
    def loadSignal(self, fname):
        with open( join(expanduser('.'), 'data', fname), 'rb') as f:                
            data = pickle.load( f)
            self.__init__(data["shot"], data["_refname"])
            for item in data:
                setattr(self, item, data[item])
        self._sigready = True

    def __set_default_window( self, B0):
        bnom = int(100*B0)
        isv = self.istart['v']
        isw = self.istart['w']
        bandstr = reduce( lambda x,y:x+y, self.bands)
        if bandstr == 'qv':
            if bnom > 170:
#              xi = [0, isq,   900,  1650, 1999]      ?! isq ????
#              f_low = [11.67, 11.67, 5.33, 5.33]
#              f_high = [33.3, 33.3,  41.7, 17.0]
               xi = array([0,  900,  1650, 1999])
               f_low = array([11.67, 5.33, 5.33])
               f_high = array([33.3,  41.7, 17.0])
               self.window['q'] = [xi[1:]-xi[:-1], f_low, f_high]
###               xi = array([0, 2048])
###               f_low = array([15.06])
###               f_high = array([27.0]) 
               xi = array([0, isv,  500, 1999])
               f_low = array([7.0,  7.0,  5.33])
               f_high = array([27.0, 27.0, 27.0])
               self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
            else:
#               xi = [0, isq,  200,  1650, 1999]      ?! isq ????
#               f_low = [8.0, 8.0,  5.33 ,5.33]
#               f_high = [33.3, 33.3, 25.0, 17.0]
                xi = array([0, 200,  1650, 1999])
                f_low = array([8.0,  5.33 ,5.33])
                f_high = array([33.3, 25.0, 17.0])
                self.window['q'] = [xi[1:]-xi[:-1], f_low, f_high]
                xi = array([0,    isv,  500,  1500, 1999])
                f_low = array([6.0,  6.0,  5.33, 7.0])
                f_high = array([27.0, 27.0, 27.0, 27.0])
                self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
        elif bandstr == 'vw':
            if (self.ioff['w']+1)//(self.ioff['v']+1) == 2:
                if bnom > 288:
                    xi = array([0, isv, 500, 1300, 1999])
                    f_low = array([11.8, 11.8,   5.7,  5.7])
                    f_high = array([35.7, 35.7,   41.7, 23.7])
                    self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isw, 1100, 2600, 3200, 3999])
                    f_low = array([4.6,  2.8, 3.5,  7.0,  10.0])
                    f_high = array([20.8, 16.8, 20.8, 25.0, 25.0])
                    self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
                elif bnom > 278:
                    xi = array([0, isv, 1100, 1200, 1800, 1999])
                    f_low = array([11.8, 11.8, 5.7, 5.7, 5.7])
                    f_high = array([35.7, 35.7, 41.7, 20.0, 13.0])
                    self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isw, 450,  570, 1000, 1200, 2600, 3200, 3999])
                    f_low = array([4.6, 7.0, 7.9,  6.8, 8.0,  9.0,  9.0,  15.0])
                    f_high = array([45.0, 45.0, 45.0, 45.0,45.0, 45.0, 45.0, 45.0])
                    self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
                elif bnom > 238:
                    xi = array([0, isv, 500, 900, 1700, 1999])
                    f_low = array([11.8, 11.8, 5.7,  5.7,  4.0])
                    f_high = array([35.7, 35.7, 41.7, 41.7, 20.8])
                    self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isw, 2100, 2600, 3200, 3999])
                    f_low = array([4.6, 4.6, 3.5, 7.0, 10.0])
                    f_high = array([20.8, 20.8, 20.8, 25.0, 25.0])
                    self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
                else:
                    xi = array([0,  isv, 500,  900,  1700, 1999])
                    f_low = array([11.8, 6.0,  5.7,  5.7,  4.0])
                    f_high = array([35.7, 35.7, 41.7, 41.7, 20.8])
                    self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isw, 400,  700, 1050, 2000, 2800, 3200, 3999])
                    f_low = array([4.6, 4.6, 6.5,  4.6, 11.0, 16.0, 39.0, 31.0])
                    f_high = array([20.8, 20.8, 20.8,20.8, 30.0, 30.0, 70.0, 50.0])
                    self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
            else:
                if bnom > 288:
                    xi = array([0, isv, 500,  1300, 1999])
                    f_low = array([11.8, 11.8,   5.7,  5.7])
                    f_high = array([35.7, 35.7,   41.7, 46.7])
                    self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isw, 550, 1300, 1600, 1999])
                    f_low = array([9.1, 5.6,    7.0, 14.0, 20.0])
                    f_high = array([41.7,33.7,   41.7,50.0, 50.0])
                    self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
                elif bnom > 278:
                    xi = array([0, isv, 500,  1200, 1999])
                    f_low = array([11.8, 11.8,   5.7,  5.7])
                    f_high = array([35.7, 35.7,   41.7, 27.7])
                    self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isw, 550, 1300, 1600, 1999])
                    f_low = array([9.1, 5.61,   7.0,  14.0, 20.0])
                    f_high = array([41.7,33.7,   41.7, 50.0, 50.0])
                    self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
                else:
                    xi = array([0, isv, 500,  900,  1999])
                    f_low = array([11.8, 11.8,   5.7,  5.7])
                    f_high = array([35.7, 35.7,   41.7, 41.7])
                    self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isw,  550, 1300, 1600, 1999])
                    f_low = array([9.1, 9.1, 7.0,  14.0, 20.0])
                    f_high = array([41.7,41.7, 41.7, 50.0, 50.0])
                    self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
        elif bandstr == 'qvw':
            if (self.ioff['w']+1)//(self.ioff['v']+1) == 2:
                if bnom > 220:
                    xi = array([0, 600,  1100,  1550, 1999])
                    f_low = array([20.0, 17.0, 10. ,5.33])
                    f_high = array([33.3, 27.0, 30., 47.0])
                    self.window['q'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isv, 500, 1999])
                    f_low = array([7.0,  7.0,  5.33])
                    f_high = array([27.0, 27.0, 27.0])
                    self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isw, 1000, 1600, 3999])
                    f_low = array([3.7,  10.4,    14.2,  13.4])
                    f_high = array([16.6, 25.0,   29.0, 35.0])
                    self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
                elif bnom > 195:
                    xi = array([0, 900,  1650, 1999])
                    f_low = array([11.67, 5.33 ,5.33])
                    f_high = array([33.3,  41.7, 17.0])
                    self.window['q'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isv,  500, 1999])
                    f_low = array([7.0,  7.0,  5.33])
                    f_high = array([27.0, 27.0, 27.0])
                    self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isw, 1000, 1600, 3999])
                    f_low = array([3.7,  10.4,    14.2,  13.4])
                    f_high = array([16.6, 25.0,   29.0, 35.0])
                    self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
                elif bnom > 185:
                    xi = array([0, 800, 1650, 1999])
                    f_low = array([11.67, 5.33 ,5.33])
                    f_high = array([33.3,  41.7, 17.0])
                    self.window['q'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isv, 500, 1999])
                    f_low = array([7.0,  7.0,  5.33])
                    f_high = array([27.0, 27.0, 27.0])
                    self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isw, 500,  570,  1050, 1200, 1600, 3999])
                    f_low = array([11.0, 12.0,   14.0, 12.0, 18.0, 14.0, 11.0])
                    f_high = array([25.0, 25.0,   25.0, 25.0, 30.0, 30.0, 35.0])
                    self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
                elif bnom > 170:
                    xi = array([0, 900, 1650, 1999])
                    f_low = array([11.67, 5.33 ,5.33])
                    f_high = array([33.3,  41.7, 17.0])
                    self.window['q'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isv,  500, 1999])
                    f_low = array([7.0,  7.0,  5.33])
                    f_high = array([27.0, 27.0, 27.0])
                    self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isw, 1000, 1600, 3999])
                    scilow = array([3.7,  6.4, 7.2,  6.4])
                    f_high = array([16.6, 25.0, 23.0, 25.0])
                    self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
                else:
                    xi = array([0, 200, 1650, 1999])
                    f_low = array([8.0, 5.33 ,5.33])
                    f_high = array([33.3,25.0, 17.0])
                    self.window['q'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isv, 500, 1500, 1999])
                    f_low = array([6.0,  6.0,  5.33, 7.0])
                    f_high = array([27.0, 27.0, 27.0, 27.0])
                    self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                    xi = array([0, isw, 1000, 1600, 3999])
                    f_low = array([3.7,  6.4,    7.2,  6.4])
                    f_high = array([50., 50.0,   50.0, 50.0])
                    self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
            else:
                xi = array([0, 900, 1650, 1999])
                f_low = array([11.67, 5.33 ,5.33])
                f_high = array([33.3,  41.7, 17.0])
                self.window['q'] = [xi[1:]-xi[:-1], f_low, f_high]
                xi = array([0, isv, 500, 1999])
                f_low = array([7.0,  7.0,  5.33])
                f_high = array([27.0, 27.0, 27.0])
                self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
                xi = array([0, isw, 500, 800, 1999])
                f_low = array([7.4, 11.2, 14.5, 12.7])
                f_high = array([33.3, 40.0,    45.0, 50.0])
                self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]

    def setScale( self, band='q', scale_params=(3., 32, 0.01)):
        self.scale[band] = self.__calc_scale( *scale_params)
        return

    def __calc_scale( self, start_scale, num_of_scale, d_scale):
        return (start_scale/(1. - start_scale*d_scale*arange(num_of_scale)))#.astype(float32)

    def __prepare_data(self, bandstr, idxlist=None):     
        fourier_period = 4*pi/(s_omega0 + sqrt(2. + s_omega0**2))
        l_scale = []
        l_iwindow = []
        for band in self.bands:
            win = self.window[band]
            win_dxi = win[0]
            win_sclow = self.fSample[band]/win[2]/fourier_period
            win_schigh = self.fSample[band]/win[1]/fourier_period
#            print win_dxi, win_sclow, win_schigh
            sc_min = min( win_sclow)
            sc_max = max( win_schigh)
            nscale = self.nscale[band]
            dscale = (1./sc_min - 1./sc_max)/(nscale - 1)
            scale = self.__calc_scale( sc_min, nscale, dscale)
            
            #if sum(win_dxi) < self.signal[band].shape[1] - 1:
            #    win_dxi = concatenate([win_dxi, array([self.signal[band].shape[1] - 1 - sum(win_dxi)]) ])
            #    win_sclow = concatenate([win_sclow, array([ sc_min])])
            #    win_schigh = concatenate([win_schigh, array([ sc_max])])
#            print sc_min, nscale, dscale 
            l_scale.append( scale)
            isclow = [*map( lambda x : x[0] if x != [] else scale.size-1, [ nonzero( scale >= sclow)[0] for sclow in win_sclow ])]
            ischigh = [*map( lambda x : x[-1] if x != [] else 0, [ nonzero( scale <= schigh)[0] for schigh in win_schigh ])]
            l_iwindow.append( array( [ list(win_dxi), isclow, ischigh])) 
        if idxlist == None:
            l_data = [ self.signal[band] for band in self.bands]
        else:
            l_data = [ self.signal[band][[*idxlist]] for band in self.bands]
        return l_data, l_scale, l_iwindow

    def calcProfile(self, idxlist = None):
        bandstr = reduce( lambda x,y:x+y, self.bands)
        l_data, l_scale, l_iwindow = self.__prepare_data( bandstr, idxlist)
        if (self.withgpu and _is_pycuda):
            l_gpCWT = gpCwtMorlet(l_data, l_scale)
            l_gpdphase, l_gpistop = gpRecoverDPhase( l_gpCWT, l_scale, l_iwindow, self.ph0ref, self.nHead, bandstr)
            gpicut = gpGetCutoff( l_gpdphase[0], self.iant, self.iend[bandstr[0]])
            gpr, gpn, gpnlen = gpCalcDensity( l_gpdphase, gpicut, l_gpistop, self.faxis, self.istart, self.iend, self.B0, self.fSample, bandstr)            
            l_prof = []
            ra = gpr.get()
            na = gpn.get()
            for ii, nn in enumerate( gpnlen.get()):
                l_prof.append( vstack(( ra[ii,:nn-1], na[ii,:nn-1])) )
        else:
            l_CWT = _CwtMorlet(l_data, l_scale)
            l_dphase, _, l_istop =  _RecoverDPhase( l_CWT, l_scale, l_iwindow, self.ph0ref, self.nHead, bandstr)
            icut = _GetCutoff( l_dphase[0], self.iant)
            l_r, l_n = _CalcDensity( l_dphase, icut, l_istop, self.faxis, self.istart, self.iend, self.B0, self.fSample, bandstr)            
            l_prof = [*map(vstack,  zip(l_r, l_n))]    
        return l_prof

    def getSpectrogram(self, band, idxlist = None):
        bandstr = reduce( lambda x,y:x+y, self.bands)
        fourier_period = 4*pi/(s_omega0 + sqrt(2. + s_omega0**2))
        idx = bandstr.index(band)
        l_data, l_scale, l_iwindow = self.__prepare_data( bandstr, idxlist)
        if (self.withgpu and _is_pycuda):
            l_gpCWT = gpCwtMorlet(l_data, l_scale)
            CWT = l_gpCWT[idx].get()
            nx = CWT.shape[1]
            ns = l_scale[idx].size
            return CWT.reshape((-1,ns,nx)), self.fSample[band]/l_scale[idx]/fourier_period
        else:
            l_CWT = _CwtMorlet(l_data, l_scale)
            return l_CWT[idx], self.fSample[band]/l_scale[idx]/fourier_period

    def getPeaktrace(self, band, idxlist = None):
        bandstr = reduce( lambda x,y:x+y, self.bands)
        l_data, l_scale, l_iwindow = self.__prepare_data( bandstr, idxlist)
        idx = bandstr.index(band)
        if (self.withgpu and _is_pycuda):
            l_gpCWT = gpCwtMorlet(l_data, l_scale)
            l_gpipeak = gpGetPeaktrace( l_gpCWT, l_scale, l_iwindow, self.nHead, bandstr)
            return l_gpipeak[idx].get()
        else:
            l_CWT = _CwtMorlet(l_data, l_scale)
            _, l_ipeak, _ =  _RecoverDPhase( l_CWT, l_scale, l_iwindow, self.ph0ref, self.nHead, bandstr)
            return l_ipeak[idx]
        
    def calcPhaseData(self, idxlist = None):
        bandstr = reduce( lambda x,y:x+y, self.bands)
        l_data, l_scale, l_iwindow = self.__prepare_data( bandstr, idxlist)
        if (self.withgpu and _is_pycuda):
            l_phasedata = []
            #gpr, gpn, gpnlen = gpCalcDensity( l_gpdphase, gpicut, l_gpistop, self.faxis, self.istart, self.iend, self.B0, self.fSample, bandstr)            
            #l_prof = []
            #ra = gpr.get()
            #na = gpn.get()
            #for ii, nn in enumerate( gpnlen.get()):
            #    l_prof.append( vstack(( ra[ii,:nn-1], na[ii,:nn-1])) )
        else:
            l_CWT = _CwtMorlet(l_data, l_scale)
            l_dphase, _, l_istop =  _RecoverDPhase( l_CWT, l_scale, l_iwindow, self.ph0ref, self.nHead, bandstr)
            icut = _GetCutoff( l_dphase[0], self.iant)
            frq_data, ph_data = _SetPhaseData( l_dphase, icut, l_istop, self.faxis, self.istart, self.iend, self.B0, self.fSample, bandstr) 
            l_phasedata = [*map(vstack,  zip(frq_data, ph_data))]    
        return l_phasedata, l_dphase, icut
    
    def genIdealSignal(self, idxlist = None):
        bandstr = reduce( lambda x,y:x+y, self.bands)
        l_data, l_scale, l_iwindow = self.__prepare_data( bandstr, idxlist)
#        if (self.withgpu and _is_pycuda):
#            l_gpCWT = gpCwtMorlet(l_data, l_scale)
#            l_gpdphase, l_gpistop = gpRecoverDPhase( l_gpCWT, l_scale, l_iwindow, self.ph0ref, self.nHead, bandstr)
#            gpicut = gpGetCutoff( l_gpdphase[0], self.iant, self.iend[bandstr[0]])
#            l_gpdphase = gpadd_refph0( l_gpdphase, self.ph0ref)
#        else:
        l_CWT = _CwtMorlet(l_data, l_scale)
        l_phase, _, l_istop =  _RecoverDPhase( l_CWT, l_scale, l_iwindow, self.ph0ref, self.nHead, bandstr)
        icut = _GetCutoff( l_phase[0], self.iant)
        for iband, band in enumerate( bandstr):
            n = min(l_phase[iband].shape[1], self.ph0ref[band].size)
            l_phase[iband][:,:n]  = cumsum(l_phase[iband][:,:n] + self.ph0ref[band][:n], axis = 1)
            if (iband == 0):
                for ii, iicut in enumerate(icut):
                    l_phase[iband][ii,:iicut] = l_phase[iband][ii,iicut]
        l_signal = [*map( sin, l_phase)]
        return dict(zip(bandstr, l_signal))

# class for mds+ interface 

try: 
    from KSTARMDSplus import KSTARMDSplus

    class KSTARreflectometer( KSTARMDSplus):
    
        def __init__(self, shot=None, band='q'):
            KSTARMDSplus.__init__(self, shot, server="172.17.250.21:8005")
            self.band = band
            
        def set_mdsplus( self, tree='KSTAR'):
            if self.alist["isopen"]:
                if self.alist["tree"].upper() != tree.upper():
                    shot = self.alist["shot"]                
                    self.close()
                    self.open(shot=shot, tree=tree)
                else:
                    pass
            else:
                self.open(shot=self.alist["shot"], tree=tree)      
           
        def get_ifinfo(self, band='q'):
            self.set_mdsplus( tree='KSTAR')
            if band == 'q':
                nodestr = '\if_qx:foo'
            elif band == 'v':
                nodestr = '\if_vx:foo'
            elif band == 'w':
                nodestr = '\if_wx:foo'
            else:
                raise Exception("Error: bad band flag")
            nch_ifxx = self.get_data(nodestr, '[0]').size
            if nch_ifxx == 1:
                t = self.get_time(nodestr)
                leap =  nonzero(t[1:]-t[:-1] > 2*(t[1]-t[0]))[0]        
                ndx_list = [0]+list(leap+1)+[t.size]
            elif nch_ifxx > 1:
                ndx_list = []
            else:
                raise Exception("Errror in data")
            return nch_ifxx, ndx_list
                 
        def get_timelist(self, band = 'q'):
            if band == 'q':
                nodestr = '\\vco_qx:foo'
            elif band == 'v':
                nodestr = '\\vco_vx:foo'
            elif band == 'w':
                nodestr = '\\vco_wx:foo'
            else:
                raise Exception("Error: bad band flag")
            self.set_mdsplus( tree='KSTAR')
            nch_ifxx, segndxlist = self.get_ifinfo( band)
            time = []
            segndata = []
            Ipdata = []
            if nch_ifxx == 1:
                for i, ndx in enumerate(segndxlist[:-1]):
                    tmpt0 = self.get_time( nodestr, '[%d]' %(segndxlist[i]))
                    tmpt1 = self.get_time( nodestr, '[%d]' %(segndxlist[i+1]-1))
                    Ip = - self.get_data('\PCRC03[%.3f]' %(tmpt0))
                    #print 'at', tmpt0, 'sec.', 'Ip = %.2f kA' %(Ip/1E3)
                    time.append([tmpt0,tmpt1])
                    segndata.append(segndxlist[i+1]-segndxlist[i] - 1)
                    Ipdata.append( Ip)
            else:
                for i in range(nch_ifxx):
                    tmptarr = self.get_time( nodestr + '%d' %(i))
                    Ip = - self.get_data('\PCRC03[%.3f]' %(tmptarr[0]))
                    #print 'at', tmptarr[0], 'sec.', 'Ip = %.2f kA' %(Ip/1E3)
                    time.append([tmptarr[0], tmptarr[-1]])
                    segndata.append(tmptarr.size)
                    Ipdata.append( Ip)
            return array(time), array(segndata), array(Ipdata)
    
        def get_timeinfo(self, band = 'q', segidx = 0):
            if band == 'q':
                nodestr = '\\vco_qx:foo'
            elif band == 'v':
                nodestr = '\\vco_vx:foo'
            elif band == 'w':
                nodestr = '\\vco_wx:foo'
            else:
                raise Exception("Error: bad band flag")
            self.set_mdsplus( tree='KSTAR')
            nch_ifxx, segndxlist = self.get_ifinfo( band)
            if nch_ifxx == 1:
                t0 = self.get_time( nodestr, '[%d]' %(segndxlist[segidx]))
                t1 = self.get_time( nodestr, '[%d]' %(segndxlist[segidx+1]-1))
                ndata = segndxlist[segidx+1]-segndxlist[segidx] - 1
                Ip = - self.get_data('\PCRC03[%.3f]' %(t0))
            else:
                tmptarr = self.get_time( nodestr + '%d' %(segidx))
                t0 = tmptarr[0]
                t1 = tmptarr[-1]
                ndata = tmptarr.size
                Ip = - self.get_data('\PCRC03[%.3f]' %(tmptarr[0]))
            if Ip < 40.0E3:
                raise Exception('Ip is too low (%.2 kA)' %(Ip*1E3))
            time = array([t0, t1])
            return time, ndata
                
        def averagetf( self, t1, t2):
            self.set_mdsplus( tree='PCS_KSTAR')
            time, It = self.get_sig('\PCITFMSRD')
            if t2 < t1:
                raise Exception("Error in paramaters")
            idx = nonzero((time >= t1) & (time <= t2) )[0]
            return It[idx[0]:idx[-1]].mean()*16*56*2E-7/1.8             
            
        def find_start( self, vco_data):
            idxflag = vco_data > vco_data.max()*.85
            idxflag[0] = False
            imin = nonzero(~idxflag[:-1]  & idxflag[1:])[0][0]
            imax = nonzero(idxflag[:-1]  & ~idxflag[1:])[0][0]
            dseg = vco_data[imin:imax+1]
            p2 = (imin, dseg[0])
            p3 = (imax, dseg[-1])
            A0 = .5* max( [ (i+imin)*(p2[1]-p3[1]) + p2[0]*(p3[1] - y) + p3[0]*(y - p2[1]) for i, y in enumerate(dseg) ])
            A1 = sum(dseg) - .5*(dseg[0] + dseg[-1])*(imax-imin)
            # check whether tranzoid or triangular
            if A1/A0 >  1.2:
                ns = len(dseg)//2
                dseg = dseg[ns:]
                imin = imin + ns
            # find the minium residual of bisectional regression
            nn = len(dseg)
            n1 = 0; n2 = nn
            while n2 - n1 > 2:
                nt1 = int(2*n1+n2)//3
                nt2 = int(n1+2*n2)//3
#              
                x1 = range(nt1);  x2 = range(nt1, nn)
                y1 = dseg[:nt1];  y2 = dseg[nt1:]
                rs1 = polyfit(x1, y1, deg=min(3, len(x1)), full=True)[1] + polyfit(x2, y2, deg=min(3, len(x2)), full=True)[1]
#              
                x1 = range(nt2);  x2 = range(nt2, nn)
                y1 = dseg[:nt2];  y2 = dseg[nt2:]
                rs2 = polyfit(x1, y1, deg=min(3, len(x1)), full=True)[1] + polyfit(x2, y2, deg=min(3, len(x2)), full=True)[1]
           
                if rs1 > rs2:
                    n1 = nt1
                    upper = False
                else:
                    n2 = nt2
                    upper = True
            return imin + (n2 if upper else n1)
        
        def read_data(self, band, iseg, ndata):
            if band == 'q':
                vco_nodestr = '\\vco_qx:foo'
                data_nodestr = '\if_qx:foo'
            elif band == 'v':
                vco_nodestr = '\\vco_vx:foo'
                data_nodestr = '\if_vx:foo'
            elif band == 'w':
                vco_nodestr = '\\vco_wx:foo'
                data_nodestr = '\if_wx:foo'
            else:
                raise Exception("Error: bad band flag")
            nch_ifxx, ndx_list = self.get_ifinfo( band)
            if nch_ifxx == 1:
                nseg = []
                for i, ndx in enumerate( ndx_list[:-1]):
                    nseg.append(ndx_list[i+1]- ndx_list[i] - 1)
                segidx = [0] + list(cumsum(nseg))
                vco_idxstr = '[%d:%d]' %(segidx[iseg], segidx[iseg]+9999)
                data_idxstr = '[%d:%d]' %(segidx[iseg], segidx[iseg]+ndata-1)
            else:
                vco_idxstr = '[0:9999]'
                vco_nodestr = vco_nodestr + '%d' %(iseg)
                data_idxstr = '[0:%d]' %(ndata-1)
                data_nodestr = data_nodestr + '%d' %(iseg)
            self.set_mdsplus( tree='KSTAR')
            vco_data = self.get_data(vco_nodestr, vco_idxstr)
            istart = self.find_start( vco_data)
            if self.alist["shot"] > 3800:
                self.set_mdsplus( tree='KSTAR')
            else:
                self.set_mdsplus( tree='R_ELECTRON')
            data = self.get_data( data_nodestr, data_idxstr)
            return data, istart
        
        def read_vco(self, band, iseg, ndata):
            if band == 'q':
                vco_nodestr = '\\vco_qx:foo'
            elif band == 'v':
                vco_nodestr = '\\vco_vx:foo'
            elif band == 'w':
                vco_nodestr = '\\vco_wx:foo'
            else:
                raise Exception("Error: bad band flag")
            nch_ifxx, ndx_list = self.get_ifinfo( band)
            if nch_ifxx == 1:
                nseg = []
                for i, ndx in enumerate( ndx_list[:-1]):
                    nseg.append(ndx_list[i+1]- ndx_list[i] - 1)
                segidx = [0] + list(cumsum(nseg))
                vco_idxstr = '[%d:%d]' %(segidx[iseg], segidx[iseg]+ndata-1)
            else:
                vco_idxstr = '[0:9999]'
                vco_nodestr = vco_nodestr + '%d' %(iseg)
            data = self.get_data( vco_nodestr, vco_idxstr)
            return data
        
except:
    _is_KSTARonline = False
    
def synIdealSignal( refprof, band, l_data ):
    """
    prof : density_profile object for reference
    l_data : list of 2xn arrays (density profiles)
    """
    if not band in refprof.bands:
        raise Exception("{:s} band is not available".format(band))
    l_signal = []
    l_phase = []
    faxis = refprof.faxis[band]
    for d in l_data:
        data = copy(d)
        fc =ce/data[0]*refprof.B0*Rmajor
        data[1] = data[1]*pp
        data = vstack((data, data[1], fc))       
        phdata = []
        ph = 0.0
        for f in faxis:
            data[2] = f*f*1e18 - fc*f*1e9 
            subdata = array([*filter(lambda x : x[1] < x[2], list(data.T))]).T
            if subdata.size != 0 :
                try:
                    n = nonzero(data[1] > data[2] )[0][0]
                except:
                    phdata.append(ph)
                else:
                    subdata = subdata[:,:n]
                    r_1, fp2_1, ffp2_1 = data[:3,n-1]; r_2, fp2_2, ffp2_2 = data[:3,n]
                    df2 = fp2_2 - ffp2_2; df1 = ffp2_1 - fp2_1
                    r0 = r_2 + (r_1-r_2)*df2/(df1+df2)
                    ra = subdata[0]
                    fp2a = subdata[1]
                    fc2a = subdata[3]**2
                    fca =  subdata[3]
                    f2 = f*f*1e18
                    #myu = array([ 1. if fp2 < 1e-8 else sqrt(1. - fp2/f2*(f2-fp2)/(f2-fp2-fc2a[ii])) for ii, fp2 in enumerate(fp2a)])
                    myu = array([ 1. if fp2 < 1e-8 else sqrt((f2+fca[ii]*f*1e9-fp2)*(f2-fca[ii]*f*1e9-fp2)/(f2-fp2-fc2a[ii])) for ii, fp2 in enumerate(fp2a)])
                    ph = 4e-9*pi/c*(sum(.5*(myu[1:]+myu[:-1])*(ra[:-1]-ra[1:])) + 2.*myu[-1]*(ra[-1]-r0)/3.) 
                    phdata.append(ph) 
            else:
                phdata.append(ph)
        df = faxis[-1] - faxis[0] 
        ph0corr = - 4.*pi/c*df/dt_sweep/refprof.fSample[band]*(data[0].max() - rin)*arange(faxis.size)  + cumsum(refprof.ph0ref[band])
        fcut = ce/data[0].max()*refprof.B0*Rmajor
        try:
            icut = nonzero(faxis*1e9 > fcut)[0][0]
            ph0corr[:icut] = 0.0
        except:
            pass
        l_signal.append(sin(array(phdata) + ph0corr))
        l_phase.append(array(phdata))
    return l_signal, l_phase
