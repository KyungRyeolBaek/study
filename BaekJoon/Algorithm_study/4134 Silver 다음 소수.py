import sys
import math


# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False # 2 이하 소수 아님
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


input = sys.stdin.readline
N = [int(input()) for _ in range(int(input()))]
for n in N:
    if n in [0, 1]:
        print(2)
    else:
        for num in range(n, int(4e9 + 10)):
            if is_prime_number(num):
                print(num)
                break

'''
# 다음 소수 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 30346 | 8007 | 6338 | 24.827% |

## 문제

정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

## 출력

각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.

## 예제 입력 1

```
3
6
20
100

```

## 예제 출력 1

```
7
23
101

```

## 출처

[Contest](https://www.acmicpc.net/category/45) > [Waterloo's local Programming Contests](https://www.acmicpc.net/category/98) > [15 July, 2012](https://www.acmicpc.net/category/detail/471) B번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [브루트포스 알고리즘](https://www.acmicpc.net/problem/tag/125)
- [정수론](https://www.acmicpc.net/problem/tag/95)
- [소수 판정](https://www.acmicpc.net/problem/tag/9)

## 메모

아.. 소수 판별 함수로 풀면 됨.

그런데 예외 처리 제대로 해야함. 최소, 최대 소수값 잘 찾기…

[소수 판별](https://www.notion.so/7ef40f8788104ac98a41cd5296c8929e?pvs=21)
'''