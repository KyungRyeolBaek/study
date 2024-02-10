import sys
import math


def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


input = sys.stdin.readline
N = int(input().strip())
result = 0
for num in map(int, input().strip().split()):
    if is_prime_number(num):
        result += 1
print(result)

'''
# 소수 찾기

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 128 MB | 197284 | 93274 | 74568 | 47.164% |

## 문제

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

## 입력

첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

## 출력

주어진 수들 중 소수의 개수를 출력한다.

## 예제 입력 1

```
4
1 3 5 7

```

## 예제 출력 1

```
3

```

## 출처

- 데이터를 추가한 사람: [bclim9108](https://www.acmicpc.net/user/bclim9108), [nova9128](https://www.acmicpc.net/user/nova9128)
- 문제의 오타를 찾은 사람: [djm03178](https://www.acmicpc.net/user/djm03178)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)
- [소수 판정](https://www.acmicpc.net/problem/tag/9)

## 메모

소수 구하는 함수.

[소수 판별](https://www.notion.so/7ef40f8788104ac98a41cd5296c8929e?pvs=21)
'''
