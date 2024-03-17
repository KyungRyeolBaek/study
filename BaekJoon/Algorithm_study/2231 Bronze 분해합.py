''' 속도 느림
# 31120KB	1288ms
import sys


input = sys.stdin.readline
N = int(input().strip())
min_value = N
for c in range(N, 1, -1):
    if N == c + sum(map(int, list(str(c)))) and min_value > c:
        min_value = c

if min_value == N:
    print(0)
else:
    print(min_value)
'''
# 31120KB	40ms
import sys


input = sys.stdin.readline
N = int(input().strip())
min_value = N
init_sum = sum(map(int, list(str(N))))
for c in range(max(N - 54, 1), max(N - init_sum + 1, N)):
    if N == c + sum(map(int, list(str(c)))) and min_value > c:
        min_value = c

if min_value == N:
    print(0)
else:
    print(min_value)

'''
# 분해합 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 192 MB | 151351 | 69945 | 55001 | 45.390% |

## 문제

어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

## 입력

첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

## 출력

첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

## 예제 입력 1

```
216

```

## 예제 출력 1

```
198

```

## 출처

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [Asia Pacific](https://www.acmicpc.net/category/42) > [Korea](https://www.acmicpc.net/category/211) > [Asia Regional - Seoul 2005](https://www.acmicpc.net/category/detail/1067) B번

- 데이터를 추가한 사람: [kimtree97](https://www.acmicpc.net/user/kimtree97), [lambda](https://www.acmicpc.net/user/lambda), [minju1307](https://www.acmicpc.net/user/minju1307), [yjwr0528](https://www.acmicpc.net/user/yjwr0528)

## 알고리즘 분류

- [브루트포스 알고리즘](https://www.acmicpc.net/problem/tag/125)

## 메모

N의 각 자리수 총 합 이하부터 시작해야 하므로 먼저 값을 낮추면 좋음

최소값을 구해야하니 오름차순으로

자연수 1,000,000이 주어지니 각자리 수 최대 값은 9 * 6 = 54 이니 N부터 54 이하로 내려갈때 까지 못찾으면 생성자가 없는것.

```python
# 31120KB	1288ms 처음 코드

# 31120KB	40ms 이후 코드
```
'''