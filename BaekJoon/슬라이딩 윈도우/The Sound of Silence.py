import sys
'''
n = 샘플 개수
m = c를 넘지 않는 연속된 샘플의 개수
c = 최소와 최대값의 차이
i = 시작점. 0이 아니라 1임.
23퍼까지.
pypy 43 틀림.
'''
from collections import deque
n, m, c = map(int, sys.stdin.readline().split())
window = list(map(int, sys.stdin.readline().split()))
indexing = [0 for _ in range(int(1e6) + 1)]
que = deque([])
length, _min, _max = 0, int(1e6), 0
silence = []
for idx in range(n):
    _next = window[idx]
    que.append(_next)
    if _next > _max:
        _max = _next
    if _next < _min:
        _min = _next
    indexing[_next] += 1
    if length < m:
        length += 1
    else:
        prev = que.popleft()
        indexing[prev] -= 1
        if indexing[prev] == 0:
            if prev == _min:
                for min_idx in range(prev, int(1e6) + 1):
                    if indexing[min_idx]:
                        _min = min_idx
                        break
            if prev == _max:
                for max_idx in range(prev, -1, -1):
                    if indexing[max_idx]:
                        _max = max_idx
                        break
    if length == m:
        if _max - _min <= c:
            silence.append(idx + 2 - m)

if silence:
    for ans in silence:
        print(ans)
else:
    print(None)
