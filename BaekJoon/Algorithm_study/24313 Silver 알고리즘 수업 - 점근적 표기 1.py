import sys


input = sys.stdin.readline
a1, a0 = map(int, input().strip().split())
c = int(input().strip())
n0 = int(input().strip())

if (c - a1) * n0 >= a0 and a1 <= c:
    print(1)
else:
    print(0)

'''
# 알고리즘 수업 - 점근적 표기 1

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 512 MB | 24389 | 8328 | 7602 | 33.895% |

## 문제

오늘도 서준이는 점근적 표기 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

알고리즘의 소요 시간을 나타내는 O-표기법(빅-오)을 다음과 같이 정의하자.

O(*g*(*n*)) = {*f*(*n*) | 모든 *n* ≥ *n0*에 대하여 *f*(*n*) ≤ *c* × *g*(*n*)인 양의 상수 *c*와 *n0*가 존재한다}

이 정의는 실제 O-표기법(https://en.wikipedia.org/wiki/Big_O_notation)과 다를 수 있다.

함수 *f*(*n*) = *a1n* + *a0*, 양의 정수 *c*, *n0*가 주어질 경우 O(*n*) 정의를 만족하는지 알아보자.

## 입력

첫째 줄에 함수 *f*(*n*)을 나타내는 정수 *a1*, *a0*가 주어진다. (0 ≤ |*ai*| ≤ 100)

다음 줄에 양의 정수 *c*가 주어진다. (1 ≤ *c* ≤ 100)

다음 줄에 양의 정수 *n0*가 주어진다. (1 ≤ *n0* ≤ 100)

## 출력

*f*(*n*), *c*, *n0*가 O(*n*) 정의를 만족하면 1, 아니면 0을 출력한다.

## 예제 입력 1

```
7 7
8
1

```

## 예제 출력 1

```
0

```

*f*(*n*) = 7*n* + 7, *g*(*n*) = *n*, *c* = 8, *n0* = 1이다. *f*(1) = 14, *c* × *g*(1) = 8이므로 O(*n*) 정의를 만족하지 못한다.

## 예제 입력 2

```
7 7
8
10

```

## 예제 출력 2

```
1

```

*f*(*n*) = 7*n* + 7, *g*(*n*) = *n*, *c* = 8, *n0* = 10이다. 모든 *n* ≥ 10에 대하여 7*n* + 7 ≤ 8*n* 이므로 O(*n*) 정의를 만족한다.

## 출처

- 문제를 검수한 사람: [chansol](https://www.acmicpc.net/user/chansol), [jhnah917](https://www.acmicpc.net/user/jhnah917), [jinhan814](https://www.acmicpc.net/user/jinhan814), [jthis](https://www.acmicpc.net/user/jthis), [leo020630](https://www.acmicpc.net/user/leo020630), [lms0806](https://www.acmicpc.net/user/lms0806), [parkky](https://www.acmicpc.net/user/parkky), [tlsdydaud1](https://www.acmicpc.net/user/tlsdydaud1), [tony9402](https://www.acmicpc.net/user/tony9402)
- 문제를 만든 사람: [MenOfPassion](https://www.acmicpc.net/user/MenOfPassion)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)

## 메모

```python
f_n = a1 * n + a0
g_n = n
f_n <= c * g_n
a1 * n + a0 <= c * n
c * n - a1 * n >= a0
```

c - a1 가 음수가 될 경우 부등호 방향이 바뀌기에 예외처리 해야함.
'''