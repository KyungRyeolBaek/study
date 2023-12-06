import sys


input = sys.stdin.readline

_min, _max = map(int, input().strip().split())
square = [s**2 for s in range(int(_max ** 0.5), int(_min ** 0.5), -1)]
if _min ** 0.5 == int(_min ** 0.5):
    square.append(_min)


answer = set()
for s in square:
    if s != 1:
        mul = set(a for a in range(s, _max, s))
        answer |= mul
answer = _max - _min + 1 - len(answer)
print(answer)
