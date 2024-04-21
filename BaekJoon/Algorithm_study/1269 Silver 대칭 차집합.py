import sys


input = sys.stdin.readline
len_A, len_B = map(int, input().strip().split())
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

print(len(A - B) + len(B - A))

'''
# 대칭 차집합

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 256 MB | 31510 | 20154 | 16751 | 64.568% |

## 문제

자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오. 두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.

예를 들어, A = { 1, 2, 4 } 이고, B = { 2, 3, 4, 5, 6 } 라고 할 때,  A-B = { 1 } 이고, B-A = { 3, 5, 6 } 이므로, 대칭 차집합의 원소의 개수는 1 + 3 = 4개이다.

## 입력

첫째 줄에 집합 A의 원소의 개수와 집합 B의 원소의 개수가 빈 칸을 사이에 두고 주어진다. 둘째 줄에는 집합 A의 모든 원소가, 셋째 줄에는 집합 B의 모든 원소가 빈 칸을 사이에 두고 각각 주어진다. 각 집합의 원소의 개수는 200,000을 넘지 않으며, 모든 원소의 값은 100,000,000을 넘지 않는다.

## 출력

첫째 줄에 대칭 차집합의 원소의 개수를 출력한다.

## 예제 입력 1

```
3 5
1 2 4
2 3 4 5 6

```

## 예제 출력 1

```
4
```

## 출처

- 문제를 만든 사람: [author5](https://www.acmicpc.net/user/author5)

## 알고리즘 분류

- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [해시를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/136)
- [트리를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/74)

## 메모

set 을 이용해서 서로의 차를 구하면 됨.

[intersection() - 교집합을 만들어 리턴](https://www.notion.so/intersection-c3df5ab1c4984026b1aa6d1edf4c0d05?pvs=21)
'''