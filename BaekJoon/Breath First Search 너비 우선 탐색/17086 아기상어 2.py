import sys
from collections import deque
input = sys.stdin.readline

shark_que = deque()
N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
for n in range(N):
    for m in range(M):
        if sea[n][m]:
            shark_que.append([n, m])


def find_safe_zone(shark_que, sea, N, M):
    direction = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    while shark_que:
        n, m = shark_que.popleft()
        for dn, dm in direction:
            nn = n + dn
            nm = m + dm
            if 0 <= nn < N and 0 <= nm < M and sea[nn][nm] == 0:
                sea[nn][nm] = sea[n][m] + 1
                shark_que.append([nn, nm])

    return sea


safe_zone = find_safe_zone(shark_que, sea, N, M)
print(max(list(map(max, safe_zone))) - 1)

# # 아기 상어 2

# | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
# | --- | --- | --- | --- | --- | --- |
# | 2 초 | 512 MB | 8730 | 4304 | 3194 | 47.242% |

# ## 문제

# N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.

# 어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.

# 안전 거리가 가장 큰 칸을 구해보자.

# ## 입력

# 첫째 줄에 공간의 크기 N과 M(2 ≤ N, M ≤ 50)이 주어진다. 둘째 줄부터 N개의 줄에 공간의 상태가 주어지며, 0은 빈 칸, 1은 아기 상어가 있는 칸이다. 빈 칸과 상어의 수가 각각 한 개 이상인 입력만 주어진다.

# ## 출력

# 첫째 줄에 안전 거리의 최댓값을 출력한다.

# ## 예제 입력 1

# ```
# 5 4
# 0 0 1 0
# 0 0 0 0
# 1 0 0 0
# 0 0 0 0
# 0 0 0 1

# ```

# ## 예제 출력 1

# ```
# 2

# ```

# ## 예제 입력 2

# ```
# 7 4
# 0 0 0 1
# 0 1 0 0
# 0 0 0 0
# 0 0 0 1
# 0 0 0 0
# 0 1 0 0
# 0 0 0 1

# ```

# ## 예제 출력 2

# ```
# 2

# ```

# ## 출처

# - 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
# - 문제의 오타를 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013)
# - 데이터를 추가한 사람: [jyn47](https://www.acmicpc.net/user/jyn47)

# ## 알고리즘 분류

# - [그래프 이론](https://www.acmicpc.net/problem/tag/7)
# - [브루트포스 알고리즘](https://www.acmicpc.net/problem/tag/125)
# - [그래프 탐색](https://www.acmicpc.net/problem/tag/11)
# - [너비 우선 탐색](https://www.acmicpc.net/problem/tag/126)

# ## 메모

# BFS로 풀면 됨.

# 상어위험도를 큐에 하나씩 넣는다.

# 넣은 상어위험도를 빼서 주변에 8방위를 조회 후 0이면 뺀 상어위험도 +1을 해서 각 방위에 넣는다.

# 다 넣으면 sea 내 최대값 조회해서 끝낸다.
