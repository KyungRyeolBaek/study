import sys


def factor(num1, num2):
    if num2 == 0:
        return num1
    else:
        return factor(num2, num1 % num2)  # 유클리드 호제법 사용


input = sys.stdin.readline
A, B = map(int, input().strip().split())
a, b = map(int, input().strip().split())
num1 = A * b + a * B
num2 = B * b

while factor(num1, num2) != 1:
    fac = factor(num1, num2)
    num1, num2 = int(num1 / fac), int(num2 / fac)

print(num1, num2)

'''
# 분수 합

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 128 MB | 34184 | 15823 | 13746 | 47.080% |

## 문제

분수 A/B는 분자가 A, 분모가 B인 분수를 의미한다. A와 B는 모두 자연수라고 하자.

두 분수의 합 또한 분수로 표현할 수 있다. 두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램을 작성하시오. 기약분수란 더 이상 약분되지 않는 분수를 의미한다.

## 입력

첫째 줄과 둘째 줄에, 각 분수의 분자와 분모를 뜻하는 두 개의 자연수가 순서대로 주어진다. 입력되는 네 자연수는 모두 30,000 이하이다.

## 출력

첫째 줄에 구하고자 하는 기약분수의 분자와 분모를 뜻하는 두 개의 자연수를 빈 칸을 사이에 두고 순서대로 출력한다.

## 예제 입력 1

```
2 7
3 5

```

## 예제 출력 1

```
31 35

```

## 출처

- 문제를 만든 사람: [author5](https://www.acmicpc.net/user/author5)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)
- [유클리드 호제법](https://www.acmicpc.net/problem/tag/26)

## 메모

약수 구해서 약수가 1이 될 때 까지 나눠주면 됨.

정답 int값으로 제출 해야함.

[Python 최대공약수, 최소공배수, 약수](https://www.notion.so/Python-bcb90a80e5e3413ab4c61e9d6547597a?pvs=21)
'''