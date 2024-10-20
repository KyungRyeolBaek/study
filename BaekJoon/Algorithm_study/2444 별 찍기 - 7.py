import sys


input = sys.stdin.readline
N = int(input().strip())
for n in range(2*N - 1):
    b = abs(N-1-n)
    print(' '*b + '*' + '*'*(2*(N - 1 - b)))

'''
# 별 찍기 - 7

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 77042 | 45099 | 40265 | 59.368% |

## 문제

예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

## 입력

첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

## 출력

첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

## 예제 입력 1

```
5

```

## 예제 출력 1

```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)

## 메모
'''