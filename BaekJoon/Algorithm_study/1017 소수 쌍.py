import sys
import math
import itertools


'''
소수 = 홀수 + 짝수
의 조건이 맞아야하기 때문에 홀수들, 짝수들 끼리 묶는다.

홀수, 짝수 쌍을 매칭하기위해 이분 매칭을 이용한다.

이분 매칭 된 쌍들이 모두 소수이면 첫번째 수에 매칭 된 숫자들 출력.
'''

# 소수 판별 함수
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# 이분 매칭
def binary_matching(left, right):
    def bimatch(N):
        if visited[N]:
            return False
        visited[N] = True

        for num in graph[N]:
            if selected[num] == -1 or bimatch(selected[num]):
                selected[num] = N
                return True

        return False

    # 왼쪽 정점수, 오른쪽 정점 수
    n, m = len(left), len(right)

    # 왼쪽 정점에서 연결 가능한 오른쪽 정점 번호들
    graph = [[i for i in range(m)] for _ in range(n)]

    # 선택된 정점 번호
    selected = [-1] * m

    for i in range(n):
        visited = [False] * (n)
        bimatch(i)
    
    
    # 결과 출력
    result = 0
    for i in range(1, m):
        if selected[i] >= 0:
            result += 1
    
    return result

# def binary_matching(left, right):
#     result = []
#     # 첫 번째 수와 매칭된 결과만 찾으면 됨.
#     N = len(left)
#     l_copy = left.copy()
#     start = l_copy.pop(0)
#     r_copy = right.copy()
#     for idx in range(N):
#         r_start = r_copy.pop(idx)
#         l_check, r_check = [True] * len(l_copy), [True] * len(l_copy)
#         if not is_prime(start + r_start):
#             continue
#         for l_idx, l in enumerate(l_copy):
#             for r_idx, r in enumerate(r_copy):
#                 if is_prime(l + r) and l_check[l_idx] and r_check[r_idx]:
#                     l_check[l_idx] = False
#                     r_check[r_idx] = False
                    



        



# 짝수 홀수 나누기.
def even_odd(_list):
    # 첫번째 값이 짝순지 홀순지 확인 후 왼쪽에 배치.
    left, right = [], []
    first_num = _list[0]
    first_num_odd = True * (first_num % 2)
    for num in _list:
        if (num % 2) == first_num_odd:
            left.append(num)
        else:
            right.append(num)
    print(left, right)
    # 짝수 홀수 개수가 같지 않으면
    if len(left) != len(right):
        return -1
    else:
        return left, right


N = int(input().strip())
lst = list(map(int, input().strip().split()))
div_list = even_odd(lst)
if div_list == -1:
    print(-1)
else:
    left, right = div_list
    right.sort()
    result = set([])
    while True:
        status = [1 for _ in range(len(right))]
        for a_idx, A in enumerate(left):
            for b_idx, (B, st) in enumerate(zip(right, status)):
                if st == 1:
                    print(A, A + B)
                    if a_idx == 0:
                        if is_prime(A + B) == True and (B not in result) == True:
                        # if a_idx == 0 and (B not in result) == True:
                            res = B
                            status[b_idx] = 0
                            break
                    if a_idx != 0:
                        if is_prime(A + B) == True:
                            status[b_idx] = 0
                            break
                        
            print(right, status)
            if sum(status) == len(right):
                break
        if sum(status) == 0:
            result.add(res)
        if sum(status) == len(right):
            break

    print(result)
    

