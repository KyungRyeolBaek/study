import sys


def factor(num1, num2):
    if num2 == 0:
        return num1
    else:
        return factor(num2, num1 % num2)  # 유클리드 호제법 사용


input = sys.stdin.readline
N = int(input())
sub = []
before = int(input())
for _ in range(N - 1):
    curr = int(input())
    sub.append(curr - before)
    before = curr

set_sub = set(sub)
fac = 0
for idx, s in enumerate(set_sub):
    if idx == 0:
        fac = s
    else:
        fac = factor(fac, s)

result = 0
for s in sub:
    result += s // fac - 1
print(result)

'''
# 가로수

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 23094 | 9393 | 7709 | 42.018% |

## 문제

직선으로 되어있는 도로의 한 편에 가로수가 임의의 간격으로 심어져있다. KOI 시에서는 가로수들이 모두 같은 간격이 되도록 가로수를 추가로 심는 사업을 추진하고 있다. KOI 시에서는 예산문제로 가능한 한 가장 적은 수의 나무를 심고 싶다.

편의상 가로수의 위치는 기준점으로 부터 떨어져 있는 거리로 표현되며, 가로수의 위치는 모두 양의 정수이다.

예를 들어, 가로수가 (1, 3, 7, 13)의 위치에 있다면 (5, 9, 11)의 위치에 가로수를 더 심으면 모든 가로수들의 간격이 같게 된다. 또한, 가로수가 (2, 6, 12, 18)에 있다면 (4, 8, 10, 14, 16)에 가로수를 더 심어야 한다.

심어져 있는 가로수의 위치가 주어질 때, 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 구하는 프로그램을 작성하라. 단, 추가되는 나무는 기존의 나무들 사이에만 심을 수 있다.

## 입력

첫째 줄에는 이미 심어져 있는 가로수의 수를 나타내는 하나의 정수 N이 주어진다(3 ≤ N ≤ 100,000). 둘째 줄부터 N개의 줄에는 각 줄마다 심어져 있는 가로수의 위치가 양의 정수로 주어지며, 가로수의 위치를 나타내는 정수는 1,000,000,000 이하이다. 가로수의 위치를 나타내는 정수는 모두 다르고, N개의 가로수는 기준점으로부터 떨어진 거리가 가까운 순서대로 주어진다.

## 출력

모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 첫 번째 줄에 출력한다.

## 예제 입력 1

```
4
1
3
7
13

```

## 예제 출력 1

```
3

```

## 예제 입력 2

```
4
2
6
12
18

```

## 예제 출력 2

```
5

```

## 출처

[Olympiad](https://www.acmicpc.net/category/2) > [한국정보올림피아드](https://www.acmicpc.net/category/55) > [한국정보올림피아드시․도지역본선](https://www.acmicpc.net/category/57) > [지역본선 2010](https://www.acmicpc.net/category/62) > [고등부](https://www.acmicpc.net/category/detail/345) 2번

- 데이터를 추가한 사람: [nhg1113](https://www.acmicpc.net/user/nhg1113), [vbder123](https://www.acmicpc.net/user/vbder123)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)
- [유클리드 호제법](https://www.acmicpc.net/problem/tag/26)

## 메모

유클리드 호제법으로 최대공약수 구해서 나무 사이간의 차이에 최대 공약수로 뺀 차이만큼 심는다.

[유클리드 호제법](https://www.notion.so/2f4feee519034a49a73a7c7cca07e677?pvs=21)
'''