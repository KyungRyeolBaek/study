import sys


# 소수면 1 아니면 0, N 값까지의 소수 찾기.
def is_prime_list(N = 1000001):
    prime = []
    check = [1] * N
    check[0] = 0
    check[1] = 0

    for i in range(2, N):
        if check[i] == 1:
            prime.append(i)
            for j in range(2*i, N, i):
                check[j] = 0
    return prime, check

T = int(sys.stdin.readline())
prime, check = is_prime_list()
for _ in range(T):
    count = 0
    N = int(sys.stdin.readline())
    for i in prime:
        if i >= N:
            break
        if check[N - i] and i <= N - i:  # 순서만 다른거 counting 하지 않기 위해
            count += 1
    print(count)

'''
# 골드바흐 파티션

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 0.5 초 | 512 MB | 28459 | 10574 | 8110 | 35.168% |

## 문제

- 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.

짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

## 입력

첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

## 출력

각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.

## 예제 입력 1

```
5
6
8
10
12
100

```

## 예제 출력 1

```
1
1
2
1
6

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [djm03178](https://www.acmicpc.net/user/djm03178)
- 문제의 오타를 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)
- [소수 판정](https://www.acmicpc.net/problem/tag/9)
- [에라토스테네스의 체](https://www.acmicpc.net/problem/tag/67)

## 메모

소수 리스트를 만들어서 체크해야 시간 초과 안뜸.

[소수 판별](https://www.notion.so/7ef40f8788104ac98a41cd5296c8929e?pvs=21)
'''