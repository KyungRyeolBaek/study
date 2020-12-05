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


# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.
# 입출력 예
# n	result
# 10	4
# 5	3
# 입출력 예 설명
# 입출력 예 #1
# 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

# 입출력 예 #2
# 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
