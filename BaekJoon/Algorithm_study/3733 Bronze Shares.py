import sys


input = sys.stdin.readline
while True:
    try:
        N, S = map(int, input().strip().split())
        print(S // (N + 1))
    except:
        break


'''
# Shares 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 8636 | 4555 | 4279 | 54.642% |

## 문제

A group of N persons and the ACM Chief Judge share equally a number of S shares (not necessary all of them). Let x be the number of shares aquired by each person (x must be an integer). The problem is to compute the maximum value of x.

Write a program that reads pairs of integer numbers from an input text file. Each pair contains the values of 1 ≤ N ≤ 10000 and 1 ≤ S ≤ 109 in that order. The input data are separated freely by white spaces, are correct, and terminate with an end of file. For each pair of numbers the program computes the maximum value of x and prints that value on the standard output from the beginning of a line, as shown in the example below.

## 예제 입력 1 복사

```
1 100
2 7
10 9
10 10

```

## 예제 출력 1 복사

```
50
2
0
0

```

## 출처

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [Europe](https://www.acmicpc.net/category/10) > [Southeastern European Regional Contest](https://www.acmicpc.net/category/12) > [SEERC 2010](https://www.acmicpc.net/category/detail/24) J번

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [사칙연산](https://www.acmicpc.net/problem/tag/121)

## 메모
'''