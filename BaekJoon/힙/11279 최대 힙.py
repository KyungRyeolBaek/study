import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    x = -int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)

# # 최대 힙

# | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
# | --- | --- | --- | --- | --- | --- |
# | 1 초 (추가 시간 없음) (https://www.acmicpc.net/problem/11279#) | 256 MB | 65108 | 30050 | 23678 | 47.902% |

# ## 문제

# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 1. 배열에 자연수 x를 넣는다.
# 2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# ## 입력

# 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 231보다 작다.

# ## 출력

# 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.

# ## 예제 입력 1

# ```
# 13
# 0
# 1
# 2
# 0
# 0
# 3
# 2
# 1
# 0
# 0
# 0
# 0
# 0

# ```

# ## 예제 출력 1

# ```
# 0
# 2
# 1
# 3
# 2
# 1
# 0
# 0

# ```

# ## 출처

# - 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
# - 데이터를 추가한 사람: [djm03178](https://www.acmicpc.net/user/djm03178), [spotky1004](https://www.acmicpc.net/user/spotky1004)

# ## 비슷한 문제

# - [1927번. 최소 힙](https://www.acmicpc.net/problem/1927)
# - [11286번. 절댓값 힙](https://www.acmicpc.net/problem/11286)

# ## 알고리즘 분류

# [보기](https://www.acmicpc.net/problem/11279#)

# ## 시간 제한

# - Java 8: 2 초
# - Java 8 (OpenJDK): 2 초
# - Java 11: 2 초
# - Kotlin (JVM): 2 초

# ## 메모

# heapq에서 최대 힙을 쓰려면 음수로 하면 된다.

# 리스트를 heap 형태로 바꾸려면 아래 코드를 사용 하면 됨.

# ```python
# heapq.heapify(list)
# ```

# heapq 종류

# ```python
# heapq.heapify(list)[0] # 가장 작은 값.
# heapq.heappop(list) # 최소값 출력
# heapq.heappush(list, x) # x를 힙에 삽입.
# ```

# 힙은 항상 완전 이진트리로 구성 되어 있기 때문에 
# 최댓값 또는 최솟값을 O(1) 안에 찾을 수 있다.
# 삽입, 삭제는 O(logN)의 시간이 걸린다.
