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
M, N = map(int, input().strip().split())
for num in range(M, N + 1):
    if is_prime_number(num):
        print(num)

'''
# 소수 구하기

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 256 MB | 278707 | 82659 | 58173 | 27.660% |

## 문제

M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

## 출력

한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

## 예제 입력 1

```
3 16

```

## 예제 출력 1

```
3
5
7
11
13

```

## 출처

- 데이터를 추가한 사람: [jinjean0123](https://www.acmicpc.net/user/jinjean0123), [yongjun042](https://www.acmicpc.net/user/yongjun042)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)
- [소수 판정](https://www.acmicpc.net/problem/tag/9)
- [에라토스테네스의 체](https://www.acmicpc.net/problem/tag/67)

## 채점 및 기타 정보

- 이 문제의 채점 우선 순위는 2이다.

## 메모

소수 판별 함수 쓰면 쉽게 품

[소수 판별](https://www.notion.so/7ef40f8788104ac98a41cd5296c8929e?pvs=21)
'''
