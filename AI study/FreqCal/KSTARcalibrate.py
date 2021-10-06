# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:06:22 2020

@author: shseo
"""
import pylab
from matplotlib import pyplot 
from numpy import *
from KSTARreflect import density_profile
from Lecroy import LeCroy_read
import KSTARmath
    
class cal_freq_scope(density_profile):
    """
    measure the real time frequency by applying a fixed frequency from
    synthesizer to LO
    Parameters
    ----------
    Samples
    -------
    x=cal_freq_scope(10,2,1,'Q',0,10780, 5000,'81126',/PLOT,QVW='qv',test=1,/spec)
    """
    def __init__( self,  shotnumber, foldnm, cIF=2, cVCO=1, dirnm='d:\\KSTAR\실적관리\\진단보고서\\2019\\Data'):#iCenter, nSample, foldname):
        super().__init__(shotnumber)
        self.cIF = cIF
        self.cVCO = cVCO
#        self.iCenter = iCenter
#        self.nSample = nSample
        self.foldnm = foldnm
        self.dirnm = dirnm
        self.width = 4000   #window for trapezoid_find_start
        self.nfaxis = 2000*25
        self.bands = 'q'
        self.period = 5000*25   #2.5 GSamples/s, 20 us + 5us +20us + 5us
#        ave = 1
#        x, v, m = LeCroy_read.readBinary(cIF, shot, foldnamm)
#        rate = round(1e-8/dt)  #ratio with the sampling rate of 100 MHz 
#        num = 2000
#        num *= rate  #data in digitizer is 2000. The scope has higher sampling rate. So more #data is needed
#        period *= rate
    
    def scope_find_start(self, level, waveform, plt=0):
        """
        find the starting point
        Samples
        -------
        iqs = scope_find_start(8.3, 3, 2)	#3=trapezoid
        """
        self.level = level
        self.waveform = waveform
#    period = 5000
#    nTail = 24
#    cutoff = -0.004
#    leW = level

        t, v, m = LeCroy_read.readBinary(self.cVCO, self.shot, self.foldnm, self.dirnm)
        iqs = KSTARmath.trapezoid_find_start(v,self.level,self.width,plt)  #the inflection point in the descending slope region
        self.iqs = int(iqs+0.5)
        self.dt = 1e6*m['HORIZ_INTERVAL']   #us
        self.fSample['q']=round(1.0/self.dt, 1)
        return(iqs)
    
    def getSignal(self, shotnumber, plt=0, bands='q', aver=0):
#    nQ = m['WAVE_ARRAY_COUNT']

        t, v, m = LeCroy_read.readBinary(self.cIF, shotnumber, self.foldnm, self.dirnm)
        self.shot = shotnumber
        nHead = self.nHead[bands]
        nsig = 2
        sig = array([ v[self.iqs-nHead+jj*self.period:self.iqs+nHead+self.nfaxis+jj*self.period] for jj in range(nsig)])
        self.signal = {bands:sig}
#        if aver:
#            pass
#        qq = stride_sum(v.y,iqs,period,ave,num)
#        else:
#            qq = v[self.iqs-self.nHead:self.iqs+self.num+self.nHead]
        if plt:
            pylab.xlabel('time ($\mu$s)') #, fontsize=20)
            pylab.plot((t[self.iqs:self.iqs+self.nfaxis]-t[self.iqs])*1e6,sig[0][nHead:-nHead])
#        super()._density_profile__set_default_window( 0 )  #B0 = 0 T for calibration
        self.__set_default_window(2500)  #fSample = 2000 MHz for 2.5 GHz oscilloscope measurements
        
    def showSignal(self, CWT, fscale, i=0, *args, **kwargs):
        amp = sqrt(CWT[i].real**2 + CWT[i].imag**2)
        self.vmax = amp.max()
        nx = CWT.shape[2]
        time = self.dt*arange(nx)
        fig=pyplot.figure( figsize=(8,4))
        pyplot.imshow(amp, *args, **kwargs)
        loc, label = pyplot.yticks() 
        pyplot.yticks( loc, [ '%.1f' %(fscale[int(n)]) for n in loc[:-1]])
        loc, label = pyplot.xticks() 
        pyplot.xticks( loc, [ '%.1f' %(time[int(n)]) for n in loc[:-1]])
        ny = fscale.size
        pyplot.xlim([0, nx-1])
        pyplot.ylim([ny-1,0])
        pyplot.xlabel('time ($\mu$s)', fontsize=20)
        pyplot.ylabel('$\Delta$f (MHz)', fontsize=20)
        return(fig)

    def __set_default_window( self, fSample):
        if fSample > 2000.0:
            xi = array([0, 25000, 50000])
            f_low = array([20.0, 20.0])
            f_high = array([1250.0, 1250.0])
            self.window['q'] = [xi[1:]-xi[:-1], f_low, f_high]
            xi = array([0, 25000, 50000])
            f_low = array([20.0, 20.0])
            f_high = array([1250.0, 1250.0])
            self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
            xi = array([0, 25000, 50000])
            f_low = array([20.0, 20.0])
            f_high = array([1250.0, 1250.0])
            self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
        elif fSample > 50.0:
            xi = array([0, 25000, 50000])
            f_low = array([20.0, 20.0])
            f_high = array([1250.0, 1250.0])
            self.window['q'] = [xi[1:]-xi[:-1], f_low, f_high]
            xi = array([0, 25000, 50000])
            f_low = array([20.0, 20.0])
            f_high = array([1250.0, 1250.0])
            self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
            xi = array([0, 25000, 50000])
            f_low = array([20.0, 20.0])
            f_high = array([1250.0, 1250.0])
            self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
        else:
            xi = array([0, 25000, 50000])
            f_low = array([20.0, 20.0])
            f_high = array([1250.0, 1250.0])
            self.window['q'] = [xi[1:]-xi[:-1], f_low, f_high]
            xi = array([0, 25000, 50000])
            f_low = array([20.0, 20.0])
            f_high = array([1250.0, 1250.0])
            self.window['v'] = [xi[1:]-xi[:-1], f_low, f_high]
            xi = array([0, 25000, 50000])
            f_low = array([20.0, 20.0])
            f_high = array([1250.0, 1250.0])
            self.window['w'] = [xi[1:]-xi[:-1], f_low, f_high]
