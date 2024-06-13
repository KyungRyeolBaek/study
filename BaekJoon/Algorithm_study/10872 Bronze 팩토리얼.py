import sys


input = sys.stdin.readline
N = int(input())
answer = 1
for n in range(1, N + 1):
    answer *= n
print(answer)

'''
# 팩토리얼

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 172297 | 94247 | 77630 | 54.954% |

## 문제

0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

## 출력

첫째 줄에 N!을 출력한다.

## 예제 입력 1

```
10

```

## 예제 출력 1

```
3628800

```

## 예제 입력 2

```
0

```

## 예제 출력 2

```
1

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)

## 메모
'''
