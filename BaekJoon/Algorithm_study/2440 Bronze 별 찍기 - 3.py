import sys


input = sys.stdin.readline
N = int(input())
for i in range(N, 0, -1):
    print('*' * i)

'''
# 별 찍기 - 3

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 100475 | 68137 | 61208 | 68.491% |

## 문제

첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

## 입력

첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

## 출력

첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

## 예제 입력 1

```
5

```

## 예제 출력 1

```
*****
****
***
**
*

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 잘못된 데이터를 찾은 사람: [cake_monotone](https://www.acmicpc.net/user/cake_monotone)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)

## 메모
'''