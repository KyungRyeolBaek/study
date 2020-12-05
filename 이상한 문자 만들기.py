def solution(s):
    return ''.join([list(s)[i].upper() if i%2==0 else list(s)[i].lower() for i in range(len(s))])
    
    
