import sys


input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    s = input().strip()
    print(s[0] + s[-1])
