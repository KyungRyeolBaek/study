import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([])
for _ in range(N):
    inputs = sys.stdin.readline().split()
    command = inputs[0]
    if command == 'push':
        queue.append(inputs[1])
    elif command == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
            
# # 큐

# | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
# | --- | --- | --- | --- | --- | --- |
# | 0.5 초 (추가 시간 없음) | 256 MB | 106305 | 48884 | 38298 | 48.910% |

# ## 문제

# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.

# - push X: 정수 X를 큐에 넣는 연산이다.
# - pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# - size: 큐에 들어있는 정수의 개수를 출력한다.
# - empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# - front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# - back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# ## 입력

# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# ## 출력

# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# ## 예제 입력 1

# ```
# 15
# push 1
# push 2
# front
# back
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# front

# ```

# ## 예제 출력 1

# ```
# 1
# 2
# 2
# 0
# 1
# 2
# -1
# 0
# 1
# -1
# 0
# 3

# ```

# ## 출처

# - 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
# - 문제의 오타를 찾은 사람: [compro0317](https://www.acmicpc.net/user/compro0317)
# - 데이터를 추가한 사람: [deunlee](https://www.acmicpc.net/user/deunlee)

# ## 알고리즘 분류

# [보기](https://www.acmicpc.net/problem/10845#)

# ## 메모

# sys.stdin.readline() 안쓰면 시간 초과 뜸.

# split 그냥 쓰면 됨. split(’ ‘)하면 실패 뜸.
