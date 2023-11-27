import sys

'''
1 부터 시작해서 k + 1이 최대로 갈 수 있는 횟수를 구하면.
경우에 따라서 남은 값 처리 하면 될듯.
total = y - x
start = 0
k = 0
while:
    if start >= total - start:
        if (total - start) % 2 == 1:
            print(k + k - 1)
        else:
            print(k + k)
    k += 1
    start += k + 1

'''
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int, input().strip().split())
    total = y - x
    start = 0
    k = 0
    while True:
        if start >= (total - start):
            if (total - start) % 2 == 1:
                print(k + k - 1)
            else:
                print(k + k)
            break
        k += 1
        start += k + 1
