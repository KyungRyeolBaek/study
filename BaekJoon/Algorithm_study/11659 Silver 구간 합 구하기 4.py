import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
num_sum = [0]
sum_all = 0
for num in nums:
    sum_all += num
    num_sum.append(sum_all)
for _ in range(M):
    i, j = map(int, input().strip().split())
    print(num_sum[j] - num_sum[i - 1])

'''
# 구간 합 구하기 4

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 124796 | 51119 | 37544 | 38.545% |

## 문제

수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

## 출력

총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

## 제한

- 1 ≤ N ≤ 100,000
- 1 ≤ M ≤ 100,000
- 1 ≤ i ≤ j ≤ N

## 예제 입력 1

```
5 3
5 4 3 2 1
1 3
2 4
5 5

```

## 예제 출력 1

```
12
9
1

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [djm03178](https://www.acmicpc.net/user/djm03178)

## 알고리즘 분류

- [누적 합](https://www.acmicpc.net/problem/tag/139)

## 메모

그냥 하면 시간초과 뜸

구간별 합을 구해서 저장해 놔야함.
'''