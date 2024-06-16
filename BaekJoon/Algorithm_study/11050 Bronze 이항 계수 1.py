import sys


def bino_coef(n, k):
    if k == 0 or n == k:
        return 1
    return bino_coef(n-1, k) + bino_coef(n-1, k-1)


input = sys.stdin.readline
print(bino_coef(*map(int, input().strip().split())))

'''
# 이항 계수 1

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 67520 | 43900 | 38030 | 64.856% |

## 문제

자연수 𝑁\(N\)과 정수 𝐾\(K\)가 주어졌을 때 이항 계수 (𝑁𝐾)\(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 𝑁\(N\)과 𝐾\(K\)가 주어진다. (1 ≤ 𝑁\(N\) ≤ 10, 0 ≤ 𝐾\(K\) ≤ 𝑁\(N\))

## 출력

(𝑁𝐾)\(\binom{N}{K}\)를 출력한다.

## 예제 입력 1

```
5 2

```

## 예제 출력 1

```
10

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)
- [조합론](https://www.acmicpc.net/problem/tag/6)

## 메모

이항 계수 재귀로 이용.

[이항 계수](https://www.notion.so/8944ad95e30d48c49cf16cb588a801d1?pvs=21)
'''