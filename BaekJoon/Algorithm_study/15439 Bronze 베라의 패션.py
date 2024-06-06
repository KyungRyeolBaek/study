import sys


input = sys.stdin.readline
N = int(input())
print(N*(N-1))

'''
# 베라의 패션 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 256 MB | 13832 | 11919 | 11380 | 86.639% |

## 문제

베라는 상의 N 벌과 하의 N 벌이 있다. i 번째 상의와 i 번째 하의는 모두 색상 i를 가진다. N 개의 색상은 모두 서로 다르다.

상의와 하의가 서로 다른 색상인 조합은 총 몇 가지일까?

## 입력

입력은 아래와 같이 주어진다.

```
N
```

## 출력

상의와 하의가 서로 다른 색상인 조합의 가짓수를 출력한다.

## 제한

- 1 ≤ N ≤ 2017
- N은 정수이다.

## 예제 입력 1

```
1

```

## 예제 출력 1

```
0

```

## 예제 입력 2

```
2

```

## 예제 출력 2

```
2

```

## 예제 입력 3

```
5

```

## 예제 출력 3

```
20

```

## 출처

[Contest](https://www.acmicpc.net/category/45) > [Waterloo's local Programming Contests](https://www.acmicpc.net/category/98) > [4 March, 2017](https://www.acmicpc.net/category/detail/1829) A번

- 문제를 번역한 사람: [kiwiyou](https://www.acmicpc.net/user/kiwiyou)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)
- [조합론](https://www.acmicpc.net/problem/tag/6)

### 메모

가지수 N * N 다음에 동일한 옷 N개 빼면 됨.
'''
