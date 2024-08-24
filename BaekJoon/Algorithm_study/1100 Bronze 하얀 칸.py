import sys


def count_F(idx, line):
    if idx % 2 == 0:
        return [line[i] for i in range(0, 8, 2)].count('F')
    else:
        return [line[i] for i in range(1, 8, 2)].count('F')


input = sys.stdin.readline
answer = 0
for idx in range(8):
    answer += count_F(idx, input().strip())

print(answer)

'''
# 하얀 칸

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 128 MB | 29022 | 20148 | 17856 | 71.794% |

## 문제

체스판은 8×8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다. 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸이다.

## 출력

첫째 줄에 문제의 정답을 출력한다.

## 예제 입력 1 복사

```
.F.F...F
F...F.F.
...F.F.F
F.F...F.
.F...F..
F...F.F.
.F.F.F.F
..FF..F.

```

## 예제 출력 1 복사

```
1

```

## 예제 입력 2 복사

```
........
........
........
........
........
........
........
........

```

## 예제 출력 2 복사

```
0

```

## 예제 입력 3 복사

```
FFFFFFFF
FFFFFFFF
FFFFFFFF
FFFFFFFF
FFFFFFFF
FFFFFFFF
FFFFFFFF
FFFFFFFF

```

## 예제 출력 3 복사

```
32

```

## 예제 입력 4 복사

```
........
..F.....
.....F..
.....F..
........
........
.......F
.F......

```

## 예제 출력 4 복사

```
2

```

## 출처

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)
- [문자열](https://www.acmicpc.net/problem/tag/158)

## 메모
'''