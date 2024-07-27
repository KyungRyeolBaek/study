import sys


def backtest(y, N, x_table, add_cross_table, sub_cross_table):
    if y == N:
        return 1
    
    result = 0

    for x in range(N):
        if x_table[x] or add_cross_table[x + y] or sub_cross_table[x - y]:
            continue
    
        x_table[x] = True
        add_cross_table[x + y] = True
        sub_cross_table[x - y] = True

        result += backtest(y + 1, N, x_table, add_cross_table, sub_cross_table)

        x_table[x] = False
        add_cross_table[x + y] = False
        sub_cross_table[x - y] = False

    return result


input = sys.stdin.readline
N = int(input())
x_table = [False] * N
add_cross_table = [False] * (2 * N)
sub_cross_table = [False] * (2 * N)

print(backtest(0, N, x_table, add_cross_table, sub_cross_table))

'''
# N-Queen

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 10 초 | 128 MB | 120272 | 57876 | 37482 | 46.637% |

## 문제

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N이 주어진다. (1 ≤ N < 15)

## 출력

첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

## 예제 입력 1

```
8

```

## 예제 출력 1

```
92

```

## 힌트

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

### 메모

x 축 체크, 대각선 체크를 y축 만큼 진행해서 문제 없으면 result + 1씩 증가.

x + y 가 같거나 x - y가 같으면 같은 대각선에 위치 함을 이용
'''