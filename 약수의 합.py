def solution(n):
    return sum([i for i in [i+1 for i in range(n)] if [i+1 for i in range(n)][-1]%i == 0])
    
