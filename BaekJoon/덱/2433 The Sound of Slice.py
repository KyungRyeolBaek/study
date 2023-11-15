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
    print('NONE')

# # The Sound of Silence 성공다국어

# | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
# | --- | --- | --- | --- | --- | --- |
# | 1 초 | 128 MB | 414 | 144 | 114 | 33.431% |

# ## 문제

# 디지털 음악에서 소리는 대기압의 변화를 나타내는 숫자로 표현한다. 대기압의 변화는 일정한 시간 구간을 정해놓고, 연속되는 구간동안 얼마나 빠르게 변했는지를 측정한다. 이렇게 측정한 값을 샘플이라고 한다.

# 음성 처리에서 가장 중요한 단계는 녹음된 소리를 사일런스 기준으로 사일런스가 아닌 구간으로 나누는 작업이다. 너무 많은 조각이 나는 것을 방지 하기 위해서 사일런스는 최저값과 최고값의 차이가 c를 넘지않는 샘플 m개의 연속이라고 정의한다.

# 샘플 n개 이루어진 레코딩과 m과 c가 주어졌을 때, 사일런스를 찾는 프로그램을 작성하시오.

# ## 입력

# 첫째 줄에 샘플의 수 n (1 ≤ n ≤ 1,000,000), m (1 ≤ m ≤ 10,000), c (0 ≤ c ≤ 10,000)가 주어진다.

# 둘째 줄에는 각 샘플의 값 ai가 주어진다. (0 ≤ ai ≤ 1,000,000 for 1 ≤ i ≤ n)

# ## 출력

# max(a[i . . . i+m−1])−min(a[i . . . i+m−1]) ≤ c를 만족하는 모든 i를 오름차순으로 한 줄에 하나씩 출력한다.

# 만약, 주어진 입력에 사일런스가 없다면, `NONE`을 출력한다.

# ## 예제 입력 1

# ```
# 7 2 0
# 0 1 1 2 3 2 2

# ```

# ## 예제 출력 1

# ```
# 2
# 6

# ```

# ## 힌트

# ## 출처

# [Olympiad](https://www.acmicpc.net/category/2) > [Baltic Olympiad in Informatics](https://www.acmicpc.net/category/6) > [BOI 2007](https://www.acmicpc.net/category/detail/235) 3번

# - 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

# ## 알고리즘 분류

# - [자료 구조](https://www.acmicpc.net/problem/tag/175)
# - [덱](https://www.acmicpc.net/problem/tag/73)
# - [슬라이딩 윈도우](https://www.acmicpc.net/problem/tag/68)

# ## 메모

# 덱을 통해 윈도우 앞부분과 뒷부분 값들을 확인 한다.

# 뒷부분의 값이 들어올 때 저장된 최대값, 최소값과 비교해서 변경 해 준다.

# 앞부분 값이 빠져나갈 때 저장된 최대값, 최소값과 비교해서 변경 해 준다.

# 최대값 최소값 차이가 c 보다 작으면 앞부분의 idx 값을 출력한다.

# 예외 처리 NONE도 출력 한다.
