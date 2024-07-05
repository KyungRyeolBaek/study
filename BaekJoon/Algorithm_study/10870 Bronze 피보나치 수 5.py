import sys


def fibonacci(n):
    if n == 0:
        return 0
    if n == (1 or 2):
        return 1
    DP = [1, 1]
    for i in range(1, n - 1):
        DP.append(DP[i] + DP[i - 1])
    return DP[n - 1]


input = sys.stdin.readline
n = int(input().strip())
print(fibonacci(n))

'''
# 피보나치 수 5

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 116056 | 70526 | 59345 | 61.164% |

## 문제

피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.

## 출력

첫째 줄에 n번째 피보나치 수를 출력한다.

## 예제 입력 1

```
10

```

## 예제 출력 1

```
55

```

## 비슷한 문제

- [2747번. 피보나치 수](https://www.acmicpc.net/problem/2747)
- [2748번. 피보나치 수 2](https://www.acmicpc.net/problem/2748)
- [2749번. 피보나치 수 3](https://www.acmicpc.net/problem/2749)
- [10826번. 피보나치 수 4](https://www.acmicpc.net/problem/10826)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)

## 메모

피보나치 수 사용 하면 됨

[피보나치](https://www.notion.so/29bb27dec1bc44d4b732abce21651471?pvs=21)
'''
