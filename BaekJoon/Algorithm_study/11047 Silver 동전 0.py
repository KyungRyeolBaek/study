import sys


input = sys.stdin.readline
N, K = map(int, input().strip().split())
coins = [int(input()) for _ in range(N)]
result = 0
for coin in coins[::-1]:
    q, r = divmod(K, coin)
    result += q
    K = r
    if K == 0:
        break

print(result)

'''
# 동전 0

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 154607 | 83165 | 63440 | 52.802% |

## 문제

준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

## 출력

첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

## 예제 입력 1

```
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

```

## 예제 출력 1

```
6

```

## 예제 입력 2

```
10 4790
1
5
10
50
100
500
1000
5000
10000
50000

```

## 예제 출력 2

```
12

```

## 출처

- 데이터를 추가한 사람: [ai4youej](https://www.acmicpc.net/user/ai4youej)
- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [그리디 알고리즘](https://www.acmicpc.net/problem/tag/33)

## 메모

큰 동전부터 나머지, 몫 구해서 계산하면 됨.

[몫과 나머지 구분 - divmod](https://www.notion.so/divmod-1149438fb762494bb9121ab5b2af3e97?pvs=21) 

[Greedy](https://www.notion.so/Greedy-2511577dc2444422bbbf3a07ab7f3151?pvs=21)
'''