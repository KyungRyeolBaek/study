import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
A = [list(map(int, input().strip().split())) for _ in range(N)]
B = [list(map(int, input().strip().split())) for _ in range(N)]
for i, bi in enumerate(B):
    for j, bj in enumerate(bi):
        A[i][j] = str(A[i][j] + bj)

for a in A:
    print(' '.join(a))

'''
# 행렬 덧셈

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 71456 | 37787 | 33033 | 53.675% |

## 문제

N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

## 입력

첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

## 출력

첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

## 예제 입력 1

```
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100

```

## 예제 출력 1

```
4 4 4
6 6 6
5 6 100

```

## 출처

- 문제의 오타를 찾은 사람: [purpose](https://www.acmicpc.net/user/purpose)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)

## 메모
'''