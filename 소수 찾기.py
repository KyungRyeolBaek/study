# 에라토스테네스의 체
# 이는 범위에 대한 소수 판별에 유리하다. 하는 방법은 다음과 같다.

# 1. 2부터 N까지의 모든 자연수를 나열한다.
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
# 3. 남은 수 중에서 i의 배수를 모두 제거한다.(i는 제거하지 않는다.)
# 4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.
import math

def solution(n):
    answer = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if answer[i] == True:
            j = 2
            while i*j <= n:
                answer[i * j] = False
                j += 1
    return len([i for i in range (2, len(answer)) if answer[i] == True])

# sqrt(n) 만큼만 해도 전부 확인 가능, ex) 16의 약수 1, 2, 4, 8, 16
  
  
# def solution(n):
#     num=set(range(2,n+1))

#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i))
#     return len(num)

# 집합 사용해서 풀이 한 내용. 
