import sys
import itertools


def factorial(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result


imput = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().strip().split())
    print(factorial(M) / factorial(N))
