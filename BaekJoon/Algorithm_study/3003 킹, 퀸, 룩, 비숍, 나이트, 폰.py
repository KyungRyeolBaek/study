import sys


input = sys.stdin.readline
set_piece = [1, 1, 2, 2, 2, 8]
piese = list(map(int, input().strip().split()))
result = list(map(str, [s_p - p for s_p, p in zip(set_piece, piese)]))
print(' '.join(result))