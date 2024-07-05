import sys


def factorial(x):
    n = 1
    for i in range(1,x+1):
        n = n*i 
    return n


input = sys.stdin.readline
N = int(input().strip())
print(factorial(N))

'''
# 팩토리얼 2

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 1024 MB | 30125 | 14070 | 12610 | 48.036% |

## 문제

0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 정수 N(0 ≤ N ≤ 20)이 주어진다.

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

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [사칙연산](https://www.acmicpc.net/problem/tag/121)

## 메모

팩토리얼 쓰면 됨.

[Python 경우의 수 팩토리얼](https://www.notion.so/Python-6b6faa99bab14c9cbc1f850e07182506?pvs=21)
'''
