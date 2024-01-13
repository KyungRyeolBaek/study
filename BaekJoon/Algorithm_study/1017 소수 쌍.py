import sys
import math
import itertools


# 소수 판별 함수
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


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