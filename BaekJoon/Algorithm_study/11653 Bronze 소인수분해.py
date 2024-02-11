import sys


input = sys.stdin.readline
N = int(input().strip())

while N != 1:
    for n in range(2, N + 1):
        q, r = divmod(N, n)
        if r == 0:
            N = q
            print(n)
            break

'''
# 소인수분해

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 107091 | 58471 | 45374 | 53.215% |

## 문제

정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

## 입력

첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

## 출력

N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

## 예제 입력 1

```
72

```

## 예제 출력 1

```
2
2
2
3
3

```

## 예제 입력 2

```
3

```

## 예제 출력 2

```
3

```

## 예제 입력 3

```
6

```

## 예제 출력 3

```
2
3

```

## 예제 입력 4

```
2

```

## 예제 출력 4

```
2

```

## 예제 입력 5

```
9991

```

## 예제 출력 5

```
97
103

```

## 출처

- 문제의 오타를 찾은 사람: [BaaaaaaaaaaarkingDog](https://www.acmicpc.net/user/BaaaaaaaaaaarkingDog), [Green55](https://www.acmicpc.net/user/Green55)
- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 잘못된 조건을 찾은 사람: [wjdclgns12](https://www.acmicpc.net/user/wjdclgns12)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)
- [소수 판정](https://www.acmicpc.net/problem/tag/9)

## 채점 및 기타 정보

- 이 문제의 채점 우선 순위는 2이다.

## 메모

divmod 사용

[몫과 나머지 구분 - divmod](https://www.notion.so/divmod-1149438fb762494bb9121ab5b2af3e97?pvs=21)
'''