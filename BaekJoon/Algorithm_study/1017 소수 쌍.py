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
    # 짝수로만 이뤄졌거나, 홀수로만 이뤄졌으면 
    if left == [] or right == []:
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
    binary_matching(left, right)






# 리스트에서 두 요소의 합이 소수인 모든 순서쌍 찾기
def find_prime_pairs(lst):
    prime_pairs = []
    for pair in itertools.combinations(lst, 2):
        if is_prime(sum(pair)):
            prime_pairs.append(pair)
    return prime_pairs


# 소수 합 순서쌍을 사용하여 전체 조합 만들기
def create_combinations(lst):
    first_num = lst[0]
    combinations, done_pairs = [], []
    prime_pairs = find_prime_pairs(lst)
    for comb in itertools.combinations(prime_pairs, len(lst)//2):
        flat_comb = sum(comb, ())
        if (flat_comb[0] == first_num) and (flat_comb[1] not in done_pairs) and len(set(flat_comb)) == N:
            combinations.append(comb)
            done_pairs.append(flat_comb[1])
    return done_pairs


N = int(input().strip())
lst = list(map(int, input().strip().split()))
result = sorted(create_combinations(lst))
if result:
    print(' '.join(map(str, result)))
else:
    print(-1)

