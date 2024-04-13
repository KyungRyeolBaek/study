import sys


input = sys.stdin.readline
N = int(input())
values = {i: 0 for i in range(int(1e4))}
for _ in range(N):
    values[int(input())] += 1
for i in range(int(1e4)):
    if values[i] != 0:
        for _ in range(values[i]):
            print(i)