import sys


input = sys.stdin.readline
N = int(input())
string_list = set([])
for _ in range(N):
    string_list.add(input().strip())

string_list = list(string_list)
string_list.sort(key=lambda x: (len(x), x))
for string in string_list:
    print(string)

'''
# 단어 정렬

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 256 MB | 183848 | 77261 | 57916 | 40.440% |

## 문제

알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로

단, 중복된 단어는 하나만 남기고 제거해야 한다.

## 입력

첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

## 출력

조건에 따라 정렬하여 단어들을 출력한다.

## 예제 입력 1

```
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

```

## 예제 출력 1

```
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate

```

## 출처

- 문제를 만든 사람: [author5](https://www.acmicpc.net/user/author5)

## 알고리즘 분류

- [문자열](https://www.acmicpc.net/problem/tag/158)
- [정렬](https://www.acmicpc.net/problem/tag/97)

## 메모

sort lambda 사용하면 쉽게 품

[Python sorted](https://www.notion.so/Python-sorted-3e3e7bf211914292b7689300b265c556?pvs=21)
'''