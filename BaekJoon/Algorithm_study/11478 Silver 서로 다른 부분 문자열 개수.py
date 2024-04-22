import sys


input = sys.stdin.readline
S = input().strip()
result = set([])
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        result.add(S[i:j])

print(len(result))

'''
# 서로 다른 부분 문자열의 개수

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 512 MB | 28266 | 17588 | 14323 | 63.089% |

## 문제

문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.

부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.

예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.

## 입력

첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.

## 출력

첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.

## 예제 입력 1

```
ababc

```

## 예제 출력 1

```
12

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [문자열](https://www.acmicpc.net/problem/tag/158)
- [해시를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/136)
- [트리를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/74)

## 메모

서로 하나씩 증가하면서 불러오면 됨.
'''