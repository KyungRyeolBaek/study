import sys


input = sys.stdin.readline
N = int(input())
members = []
for i in range(N):
    member = input().strip().split()
    member.append(i)
    members.append(member)

members.sort(key=lambda x: (int(x[0]), x[2]))
for member in members:
    print(' '.join(member[:2]))