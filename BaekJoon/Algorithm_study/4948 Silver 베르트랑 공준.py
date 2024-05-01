import sys
import math


# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False    # 2 이하 소수 아님
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False    # 소수가 아님
    return True     # 소수임


input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for num in range(n + 1, 2*n + 1):
        if is_prime_number(num):
            count += 1
    print(count)

'''
# 베르트랑 공준 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 107311 | 41906 | 33517 | 38.568% |

## 문제

베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

입력의 마지막에는 0이 주어진다.

## 출력

각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

## 제한

- 1 ≤ n ≤ 123,456

## 예제 입력 1

```
1
10
13
100
1000
10000
100000
0

```

## 예제 출력 1

```
1
4
3
21
135
1033
8392

```

## 출처

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [Asia Pacific](https://www.acmicpc.net/category/42) > [Japan](https://www.acmicpc.net/category/43) > [Japan Domestic Contest](https://www.acmicpc.net/category/44) > [2011 Japan Domestic Contest](https://www.acmicpc.net/category/detail/201) A번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)
- [소수 판정](https://www.acmicpc.net/problem/tag/9)
- [에라토스테네스의 체](https://www.acmicpc.net/problem/tag/67)

## 메모

범위 내에 소수 판별 진행 하면 됨.

[소수 판별](https://www.notion.so/7ef40f8788104ac98a41cd5296c8929e?pvs=21)
'''