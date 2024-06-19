import sys


def gcd(x, y):
    while y:
	    x, y = y, x % y
    return x


input = sys.stdin.readline
N = input()
A = list(map(int, input().strip().split()))
s = A[-1]
min_num = s
for a in A[:-1]:
    num = gcd(s, a)
    if num < min_num:
        min_num = num
    s = s * a // num
if len(A) == 0:
    print(s**2)
elif s in A:
    print(s * min_num)
else:
    print(s)

'''
# 약수

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 512 MB | 71616 | 40222 | 34914 | 56.436% |

## 문제

양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다. 둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.

## 출력

첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.

## 예제 입력 1

```
2
4 2

```

## 예제 출력 1

```
8

```

## 예제 입력 2

```
1
2

```

## 예제 출력 2

```
4

```

## 예제 입력 3

```
6
3 4 2 12 6 8

```

## 예제 출력 3

```
24

```

## 예제 입력 4

```
14
14 26456 2 28 13228 3307 7 23149 8 6614 46298 56 4 92596

```

## 예제 출력 4

```
185192

```

## 출처

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 빠진 조건을 찾은 사람: [doju](https://www.acmicpc.net/user/doju)
- 어색한 표현을 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)

## 메모

최소공배수 구하면 됨. 여러개가 있는 경우 하나씩 하면 됨.

[여러개의 최대공배수, 최소공약수 구할 때](https://www.notion.so/431dd94531be49b8b6dc855df6949635?pvs=21)
'''
