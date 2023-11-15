import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
swap_board = [['' for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        swap_board[i][j] = board[j][i]


def max_in_line(line):
    save_key, max_num, count_num = '', 0, 0
    for key in line:
        if save_key == key:
            count_num += 1
        else:
            max_num = max(max_num, count_num)
            save_key = key
            count_num = 1

    max_num = max(max_num, count_num)

    return max_num


max_value = 0

for i in range(N):
    for j in range(N):
        if i + 1 < N:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            col = [board[idx][0] for idx in range(N)]
            max_value = max(max_value, max_in_line(board[i]), max_in_line(board[i + 1]), max_in_line(col))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

for i in range(N):
    for j in range(N):
        if i + 1 < N:
            swap_board[i][j], swap_board[i + 1][j] = swap_board[i + 1][j], swap_board[i][j]
            col = [swap_board[idx][0] for idx in range(N)]
            max_value = max(max_value, max_in_line(swap_board[i]), max_in_line(swap_board[i + 1]), max_in_line(col))
            swap_board[i][j], swap_board[i + 1][j] = swap_board[i + 1][j], swap_board[i][j]

print(max_value)

'''
# 사탕 게임 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 40080 | 13734 | 9379 | 33.074% |

## 문제

상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

## 출력

첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.

## 예제 입력 1

```
3
CCP
CCP
PPC

```

## 예제 출력 1

```
3

```

## 예제 입력 2

```
4
PPPP
CYZY
CCPY
PPCC

```

## 예제 출력 2

```
4

```

## 예제 입력 3

```
5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ

```

## 예제 출력 3

```
4

```

## 힌트

예제 3의 경우 4번 행의 Y와 C를 바꾸면 사탕 네 개를 먹을 수 있다.

## 출처

[Olympiad](https://www.acmicpc.net/category/2) > [Croatian Highschool Competitions in Informatics](https://www.acmicpc.net/category/25) > [2012](https://www.acmicpc.net/category/26) > [Junior Croatian Olympiad in Informatics - Exam #1](https://www.acmicpc.net/category/detail/246)  1번

- 데이터를 추가한 사람: [10jobss](https://www.acmicpc.net/user/10jobss)
- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 문제의 오타를 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013)
- 잘못된 조건을 찾은 사람: [juhyun16](https://www.acmicpc.net/user/juhyun16)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)
- [브루트포스 알고리즘](https://www.acmicpc.net/problem/tag/125)

## 메모

일반 보드를 대치 해서 스왑 보드를 만듦.

보드의 위아래 행으로만 단어를 바꿈.

바꾼 행 두개에 연속되는 숫자의 최대 개수를 구함.

바꾼 열 한개에 연속되는 숫자의 최대 개수를 구함.

바꾼 열도 최대 개수를 구해야 했는데 안구해서 많이 틀림…

최대 개수가 더 큰 값으로 갱신함.
'''
