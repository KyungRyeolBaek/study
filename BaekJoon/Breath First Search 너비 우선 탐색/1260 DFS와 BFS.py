import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().rstrip().split())
values = [list(map(int, input().rstrip().split())) for _ in range(M)]


def bidirect_graph(values: list):
    graph = {}
    for val in values:
        k, v = val
        graph[k] = graph.get(k, []) + [v]
        graph[v] = graph.get(v, []) + [k]
        graph[k].sort()
        graph[v].sort()
    return graph


def DFS(graph, root, dfs_list=[]):
    if root not in dfs_list:
        dfs_list.append(root)
        if root in graph:
            for x in graph[root]:
                DFS(graph, x, dfs_list)

    return dfs_list


def BFS(graph, root):
    queue = deque([root])
    res = [root]
    while queue:
        start = queue.pop()
        if start in graph:
            for x in graph[start]:
                if x not in res:
                    queue.appendleft(x)
                    res.append(x)
    return res


graph = bidirect_graph(values)
print(' '.join(list(map(str, DFS(graph, V)))))
print(' '.join(list(map(str, BFS(graph, V)))))

# # DFS와 BFS

# | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
# | --- | --- | --- | --- | --- | --- |
# | 2 초 | 128 MB | 242966 | 92698 | 55142 | 37.013% |

# ## 문제

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# ## 입력

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# ## 출력

# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# ## 예제 입력 1

# ```
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# ```

# ## 예제 출력 1

# ```
# 1 2 4 3
# 1 2 3 4

# ```

# ## 예제 입력 2

# ```
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1

# ```

# ## 예제 출력 2

# ```
# 3 1 2 5 4
# 3 1 4 2 5

# ```

# ## 예제 입력 3

# ```
# 1000 1 1000
# 999 1000

# ```

# ## 예제 출력 3

# ```
# 1000 999
# 1000 999

# ```

# ## 출처

# - 문제를 만든 사람: [author5](https://www.acmicpc.net/user/author5)
# - 데이터를 추가한 사람: [dfghcvb11](https://www.acmicpc.net/user/dfghcvb11), [djm03178](https://www.acmicpc.net/user/djm03178), [doju](https://www.acmicpc.net/user/doju)
# - 어색한 표현을 찾은 사람: [doju](https://www.acmicpc.net/user/doju)
# - 빠진 조건을 찾은 사람: [pumpyboom](https://www.acmicpc.net/user/pumpyboom)

# ## 알고리즘 분류

# - [그래프 이론](https://www.acmicpc.net/problem/tag/7)
# - [그래프 탐색](https://www.acmicpc.net/problem/tag/11)
# - [너비 우선 탐색](https://www.acmicpc.net/problem/tag/126)
# - [깊이 우선 탐색](https://www.acmicpc.net/problem/tag/127)

# ## 메모

# BFS, DFS를 사용. Graph에 저장 할 때 정렬을 해야함.

# 노드에 간선이 없어도 출력 해야함.

# 이부분 때문에 계속 틀림..
