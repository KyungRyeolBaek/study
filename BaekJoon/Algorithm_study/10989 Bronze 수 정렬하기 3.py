import sys


input = sys.stdin.readline
N = int(input())
values = {i: 0 for i in range(10001)}
for _ in range(N):
    values[int(input())] += 1
for i in range(10001):
    if values[i] != 0:
        for _ in range(values[i]):
            print(i)

'''
# 수 정렬하기 3 언어 제한

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 5 초 (https://www.acmicpc.net/problem/10989#) | 8 MB (https://www.acmicpc.net/problem/10989#) | 289511 | 68738 | 52551 | 23.762% |

## 문제

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

## 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

## 출력

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

## 예제 입력 1

```
10
5
2
3
1
4
2
3
5
1
7

```

## 예제 출력 1

```
1
1
2
2
3
3
4
5
5
7

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [cgiosy](https://www.acmicpc.net/user/cgiosy)
- 문제의 오타를 찾은 사람: [joonas](https://www.acmicpc.net/user/joonas)

## 비슷한 문제

- [2750번. 수 정렬하기](https://www.acmicpc.net/problem/2750)
- [2751번. 수 정렬하기 2](https://www.acmicpc.net/problem/2751)

## 알고리즘 분류

[보기](https://www.acmicpc.net/problem/10989#)

## 제출할 수 없는 언어

node.js

## 시간 제한

- Java 8: 3 초
- Java 8 (OpenJDK): 3 초
- Java 11: 3 초
- Kotlin (JVM): 3 초
- Java 15: 3 초

## 메모리 제한

- Java 8: 512 MB
- Java 8 (OpenJDK): 512 MB
- Java 11: 512 MB
- Kotlin (JVM): 512 MB
- Java 15: 512 MB

## 채점 및 기타 정보

- 이 문제의 채점 우선 순위는 2이다.

## 메모

sort 쓰면 시간 초과 뜬다.

자리 마련해놓고 거기에 개수 세서 출력
'''