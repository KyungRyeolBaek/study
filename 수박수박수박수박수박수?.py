def solution(n):
    return ['수박'*int(n/2) if int(n%2) == 0 else ('수박'*(int(n/2)+1))[:-1]][0]
    
# 짝수면 n의 절반만큼 수박 곱하기, 홀수면 n의 절반 +1만큼 수박 곱하고 마지막 하나 빼기
