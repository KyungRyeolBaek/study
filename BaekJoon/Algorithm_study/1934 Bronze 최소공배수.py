import sys


def factor(num1, num2):
    if num2 == 0:
        return num1
    else:
        return factor(num2, num1 % num2)  # 유클리드 호제법 사용


input = sys.stdin.readline
N = int(input())
for _ in range(N):
    A, B = map(int, input().strip().split())
    print(int(A * B / factor(A, B)))

'''
# 최소공배수

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 77562 | 42346 | 36094 | 55.681% |

## 문제

두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.

두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

## 출력

첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.

## 예제 입력 1

```
3
1 45000
6 10
13 17

```

## 예제 출력 1

```
45000
30
221

```

## 출처

- 문제의 오타를 찾은 사람: [jason9319](https://www.acmicpc.net/user/jason9319), [kyo20111](https://www.acmicpc.net/user/kyo20111)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)
- [유클리드 호제법](https://www.acmicpc.net/problem/tag/26)

## 메모

최소 공배수, 최대 공약수 유클리드 호제법으로 구해서 진행.

[유클리드 호제법](https://www.notion.so/2f4feee519034a49a73a7c7cca07e677?pvs=21)
'''