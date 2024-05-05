import sys
import math


# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False    # 2 이하 소수 아님
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False    # 소수가 아님
    return True     # 소수임


input = sys.stdin.readline
T = int(input())
N_list = [int(input()) for _ in range(T)]
prime_dict = {2:True}
for num in range(1, max(N_list)//2 + 1, 2):
    prime_dict[num] = is_prime_number(num)

for N in N_list:
    count = 0
    if N >= 4 and is_prime_number(N - 2):
        count += 1
    for num in range(3, N//2 + 1, 2):
        if prime_dict.get(num, False) and is_prime_number(N - num):
            count += 1
    print(count)