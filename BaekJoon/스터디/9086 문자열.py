import sys


input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    s = input().strip()
    print(s[0] + s[-1])

'''
# 문자열 성공

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 53493 | 34533 | 31592 | 65.455% |

## 문제

문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

## 입력

입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 한 줄에 하나의 문자열이 주어진다. 문자열은 알파벳 A~Z 대문자로 이루어지며 알파벳 사이에 공백은 없으며 문자열의 길이는 1000보다 작다.

## 출력

각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.

## 예제 입력 1

```
3
ACDKJFOWIEGHE
O
AB

```

## 예제 출력 1

```
AE
OO
AB

```

## 출처

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [Asia Pacific](https://www.acmicpc.net/category/42) > [Korea](https://www.acmicpc.net/category/211) > [Nationwide Internet Competition](https://www.acmicpc.net/category/256) > [Seoul Nationalwide Internet Competition 2003](https://www.acmicpc.net/category/detail/1090) PB번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)
- [문자열](https://www.acmicpc.net/problem/tag/158)

## 메모
'''
