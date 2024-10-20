import sys


input = sys.stdin.readline

X = int(input().strip())
N = int(input().strip())
for _ in range(N):
    a, b = map(int, input().strip().split())
    X -= (a * b)

if X:
    print('No')
else:
    print('Yes')

'''
# 영수증

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 1024 MB | 105777 | 58679 | 52298 | 56.265% |

## 문제

준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.

영수증에 적힌,

- 구매한 각 물건의 가격과 개수
- 구매한 물건들의 총 금액

을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

## 입력

첫째 줄에는 영수증에 적힌 총 금액 �$X$가 주어진다.

둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 �$N$이 주어진다.

이후 �$N$개의 줄에는 각 물건의 가격 �$a$와 개수 �$b$가 공백을 사이에 두고 주어진다.

## 출력

구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 `Yes`를 출력한다. 일치하지 않는다면 `No`를 출력한다.

## 제한

- $1 ≤ X ≤ 1\,000\,000\,000$
    
    1≤�≤1000000000
    
- $1 ≤ N ≤ 100$
    
    1≤�≤100
    
- $1 ≤ a ≤ 1\,000\,000$
    
    1≤�≤1000000
    
- $1 ≤ b ≤ 10$
    
    1≤�≤10
    

## 예제 입력 1

```
260000
4
20000 5
30000 2
10000 6
5000 8

```

## 예제 출력 1

```
Yes

```

영수증에 적힌 구매할 물건들의 목록으로 계산한 총 금액은 20000 × 5 + 30000 × 2 + 10000 × 6 + 5000 × 8 = 260000원이다. 이는 영수증에 적힌 총 금액인 260000원과 일치한다.

## 예제 입력 2

```
250000
4
20000 5
30000 2
10000 6
5000 8

```

## 예제 출력 2

```
No

```

## 출처

[University](https://www.acmicpc.net/category/5) > [연세대학교 미래캠퍼스](https://www.acmicpc.net/category/541) > [2022 연세대학교 미래캠퍼스 슬기로운 코딩생활](https://www.acmicpc.net/category/detail/3136) A번

- 문제를 검수한 사람: [jhnah917](https://www.acmicpc.net/user/jhnah917), [yclock](https://www.acmicpc.net/user/yclock)
- 문제를 만든 사람: [junie](https://www.acmicpc.net/user/junie)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)
- [사칙연산](https://www.acmicpc.net/problem/tag/121)

## 메모
'''
