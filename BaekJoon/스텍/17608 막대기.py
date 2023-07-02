import sys
N = int(input())
stack = [int(sys.stdin.readline()) for _ in range(N)]

count_stick = 1
curr_stick = stack.pop()
while stack:
    next_stick = stack.pop()
    if curr_stick < next_stick:
        curr_stick = next_stick
        count_stick += 1

print(count_stick)

# # 막대기

# | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
# | --- | --- | --- | --- | --- | --- |
# | 1 초 (추가 시간 없음) | 512 MB | 19972 | 8565 | 6942 | 44.029% |

# ## 문제

# 아래 그림처럼 높이만 다르고 (같은 높이의 막대기가 있을 수 있음) 모양이 같은 막대기를 일렬로 세운 후, 왼쪽부터 차례로 번호를 붙인다. 각 막대기의 높이는 그림에서 보인 것처럼 순서대로 6, 9, 7, 6, 4, 6 이다. 일렬로 세워진 막대기를 오른쪽에서 보면 보이는 막대기가 있고 보이지 않는 막대기가 있다. 즉, 지금 보이는 막대기보다 뒤에 있고 높이가 높은 것이 보이게 된다. 예를 들어, 그림과 같은 경우엔 3개(6번, 3번, 2번)의 막대기가 보인다.

# N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성하려고 한다.

# ## 입력

# 첫 번째 줄에는 막대기의 개수를 나타내는 정수 N (2 ≤ N ≤ 100,000)이 주어지고 이어지는 N줄 각각에는 막대기의 높이를 나타내는 정수 h(1 ≤ h ≤ 100,000)가 주어진다.

# ## 출력

# 오른쪽에서 N개의 막대기를 보았을 때, 보이는 막대기의 개수를 출력한다.

# ## 예제 입력 1

# ```
# 6
# 6
# 9
# 7
# 6
# 4
# 6

# ```

# ## 예제 출력 1

# ```
# 3

# ```

# ## 예제 입력 2

# ```
# 5
# 5
# 4
# 3
# 2
# 1

# ```

# ## 예제 출력 2

# ```
# 5

# ```

# ## 출처

# [Olympiad](https://www.acmicpc.net/category/2) > [한국정보올림피아드](https://www.acmicpc.net/category/55) > [KOI 2019 1차대회](https://www.acmicpc.net/category/455) > [초등부](https://www.acmicpc.net/category/detail/2072) 1번

# ## 알고리즘 분류

# - [구현](https://www.acmicpc.net/problem/tag/102)
# - [자료 구조](https://www.acmicpc.net/problem/tag/175)
# - [스택](https://www.acmicpc.net/problem/tag/71)

# ## 메모

# input을 문자열로 받기에 int로 변환 해 줘야 한다.

# sys.stdin.readline()을 써서 입력 시간을 줄여줘야 시간 초과가 뜨지 않는다.

# input으로 받을 때 버퍼에 입력 하는 값 하나하나 저장 하는데, 

# sys.stdin.readline()은 개행 문자까지 포함된 하나의 줄을 한 번의 버퍼로 입력 받는다.
