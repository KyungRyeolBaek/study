import sys
import itertools


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    P = []
    total_x, total_y = 0, 0
    for _ in range(N):
        x, y = map(int, input().strip().split())
        total_x += x
        total_y += y
        P.append((x, y))

    result = 10**10
    combi = list(itertools.combinations(P, N // 2))
    for combi_P in combi:
        half_x1, half_y1 = 0, 0
        for x, y in combi_P:
            half_x1 += x
            half_y1 += y

        half_x2 = total_x - half_x1
        half_y2 = total_y - half_y1

        vector = ((half_x1 - half_x2)**2 + (half_y1 - half_y2)**2)**0.5
        result = min(result, vector)

    print(result)


'''
# 벡터 매칭 스페셜 저지

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 512 MB | 11614 | 4324 | 3150 | 37.469% |

## 문제

평면 상에 N개의 점이 찍혀있고, 그 점을 집합 P라고 하자. 집합 P의 벡터 매칭은 벡터의 집합인데, 모든 벡터는 집합 P의 한 점에서 시작해서, 또 다른 점에서 끝나는 벡터의 집합이다. 또, P에 속하는 모든 점은 한 번씩 쓰여야 한다.

벡터 매칭에 있는 벡터의 개수는 P에 있는 점의 절반이다.

평면 상의 점이 주어졌을 때, 집합 P의 벡터 매칭에 있는 벡터의 합의 길이의 최솟값을 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 구성되어있다.

테스트 케이스의 첫째 줄에 점의 개수 N이 주어진다. N은 짝수이다. 둘째 줄부터 N개의 줄에 점의 좌표가 주어진다. N은 20보다 작거나 같은 자연수이고, 좌표는 절댓값이 100,000보다 작거나 같은 정수다. 모든 점은 서로 다르다.

## 출력

각 테스트 케이스마다 정답을 출력한다. 절대/상대 오차는 10-6까지 허용한다.

## 예제 입력 1

```
2
4
5 5
5 -5
-5 5
-5 -5
2
-100000 -100000
100000 100000

```

## 예제 출력 1

```
0.000000000000
282842.712474619038

```

## 예제 입력 2

```
1
10
26 -76
65 -83
78 38
92 22
-60 -42
-27 85
42 46
-86 98
92 -47
-41 38

```

## 예제 출력 2

```
13.341664064126334

```

## 출처

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 문제의 오타를 찾은 사람: [eric00513](https://www.acmicpc.net/user/eric00513), [jacob_1120](https://www.acmicpc.net/user/jacob_1120)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [브루트포스 알고리즘](https://www.acmicpc.net/problem/tag/125)

## 메모

문제 이해가 어려웠던 문제.

방법은 이렇게 하면 되겠다 라고 생각이 드는데 코드 구현을 어떻게 해야 할지 고민 했던 문제.

방법.

1. 모든 x, y 좌표들의 합을 구한다.
2. 각 점의 절반에 해당 하는 부분의 x, y 좌표들의 합을 구한다.
3. 1.에서 구했던 합과 2.에서 구했던 합을 빼면 2.에서 구했던 반대 점의 절반의 x, y 좌표들의 합이 구해진다.
4. 2.에서 구한 합과 3.에서 구한 합의 벡터의 최소값을 구하면 된다.

수도 코드

```python
P = [모든 점의 좌표.]
# 1.
for x, y in P:
    total_x += x
    total_y += y

# 2.
# 최대 값에 대한 정보가 없어서 임의로 10의 10승으로 잡았음.
result = 10**10
combi = combination(B, len(P) // 2 )
# 조합의 특수한 경우(양방향이 똑같을 경우) 절반 이하는 중복되므로 반만 해두 댐.
for combi_P in combi[:len(combi) // 2]:
    for x, y in combi_P:
        half_x1 += x
        half_y1 += y

    # 3.
    half_x2 = total_x - half_x1
    half_y2 = total_y - half_y1

    # 4.
    result = min(result, ((half_x1 - half_x2)**2 + (half_y1 - half_y2)**2)**0.5)

print(result)
```
'''
