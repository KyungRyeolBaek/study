import sys


input = sys.stdin.readline
for _ in range(int(input())):
    print(sum(map(int, input().strip().split())))


'''
# Can you add this? 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 7622 | 6189 | 5917 | 81.862% |

## 문제

Given two integers, calculate and output their sum.

## 입력

The input contains several test cases. The first line contains and integer t (t ≤ 100) denoting the number of test cases. Then t tests follow, each of them consisiting of two space separated integers x and y (−109 ≤ x, y ≤ 109).

## 출력

For each test case output output the sum of the corresponding integers.

## 예제 입력 1 복사

```
4
-100 100
2 3
0 110101
-1000000000 1

```

## 예제 출력 1 복사

```
0
5
110101
-999999999

```

## 출처

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [Europe](https://www.acmicpc.net/category/10) > [Central European Regional Contest](https://www.acmicpc.net/category/13) > [CERC 2008](https://www.acmicpc.net/category/detail/951) PA번

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)
- [사칙연산](https://www.acmicpc.net/problem/tag/121)

## 메모
'''