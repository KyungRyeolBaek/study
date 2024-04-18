import sys


input = sys.stdin.readline

_min, _max = map(int, input().strip().split())
square = [s**2 for s in range(1, int(_max ** 0.5) + 1)]
set_square = set()
for s in square:
    if s != 1 and (s not in set_square):
        s_min = (_min // s) * s
        if s_min <= _max:
            mul = set([a for a in range(s_min, _max + 1, s) if (a >= _min) and (a not in set_square)])
            set_square |= mul
nono = _max - _min + 1 - len(set_square)
print(nono)

'''
# 제곱 ㄴㄴ 수 성공

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 512 MB | 59526 | 11505 | 8047 | 21.624% |

## 문제

어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 제곱수는 정수의 제곱이다. min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

## 입력

첫째 줄에 두 정수 min과 max가 주어진다.

## 출력

첫째 줄에 min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수의 개수를 출력한다.

## 제한

- 1 ≤ min ≤ 1,000,000,000,000
- min ≤ max ≤ min + 1,000,000

## 예제 입력 1

```
1 10

```

## 예제 출력 1

```
7

```

## 예제 입력 2

```
15 15

```

## 예제 출력 2

```
1

```

## 예제 입력 3

```
1 1000

```

## 예제 출력 3

```
608

```

## 출처

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)
- [소수 판정](https://www.acmicpc.net/problem/tag/9)
- [에라토스테네스의 체](https://www.acmicpc.net/problem/tag/67)

## 메모

시간 제한을 맞추기 어려웠던 문제다.

우선 여러 가지 방법으로 진행 했었는데,

1. min부터 max 까지 그 사이의 제곱수들을 구해 그 수들의 배수들을 제거 했다.
    1. 문제 이해가 틀림.
2. 1부터 max까지의 제곱수들을 구해 그 수들의 배수들을 제거 했다.
    1. 너무 시간이 오래 걸림.
3. 1부터 max까지의 제곱수들을 구하고,
제곱수 중 작은 것 부터 배수들을 구해 집합에 넣고, 
집합 내에 있는 제곱수는 pass 하면서 모든 배수들을 집합에 넣은 뒤.
min ~ max 사이 숫자의 개수와 집합의 개수의 차를 구하면 된다.
'''
