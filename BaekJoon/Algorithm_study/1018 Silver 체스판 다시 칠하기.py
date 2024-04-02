import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().strip().replace('B', '1').replace('W', '0'))))

filter_lines = [[0 if i % 2 == 0 else 1 for i in range(M)], [1 if i % 2 == 0 else 0 for i in range(M)]]
max_count = 2500
filter_height = N - 8 + 1
filter_weight = M - 8 + 1
for height in range(filter_height):
    for weight in range(filter_weight):
        for filter_count in range(2):
            count = 0
            for idx, line in enumerate(board[height:height + 8]):
                if (filter_count + idx) % 2 == 0:
                    select = 0
                else:
                    select = 1
                for value, filter_value in zip(line[weight:weight + 8], filter_lines[select][weight:weight + 8]):
                    count += abs(value - filter_value)

            if max_count > count:
                max_count = count

print(max_count)

'''
# 체스판 다시 칠하기

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 128 MB | 120888 | 59997 | 47979 | 49.793% |

## 문제

지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

## 출력

첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

## 예제 입력 1

```
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

```

## 예제 출력 1

```
1

```

## 예제 입력 2

```
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

```

## 예제 출력 2

```
12

```

## 예제 입력 3

```
8 8
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB

```

## 예제 출력 3

```
0

```

## 예제 입력 4

```
9 23
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBW

```

## 예제 출력 4

```
31

```

## 예제 입력 5

```
10 10
BBBBBBBBBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBBBBBBBBB

```

## 예제 출력 5

```
0

```

## 예제 입력 6

```
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWWWB
BWBWBWBW

```

## 예제 출력 6

```
2

```

## 예제 입력 7

```
11 12
BWWBWWBWWBWW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBWWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW

```

## 예제 출력 7

```
15

```

## 출처

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [barkstone2](https://www.acmicpc.net/user/barkstone2), [jh05013](https://www.acmicpc.net/user/jh05013)
- 문제를 다시 작성한 사람: [jh05013](https://www.acmicpc.net/user/jh05013)

## 알고리즘 분류

- [브루트포스 알고리즘](https://www.acmicpc.net/problem/tag/125)

## 메모

8 * 8 의 체스판을 만든다는 말이 이해가 처음에 잘 안갔다.

8 * 8에 맞는 보드를 하나씩 체크해가면서 체스판이 맞는지 확인 하면 됨.
'''