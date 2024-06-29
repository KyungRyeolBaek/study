import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
words = dict()
for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        words[word] = words.get(word, 0) + 1

words = sorted(words.items(), key=lambda x: (-1*x[1], -1*len(x[0]), x[0]))
for key, value in words:
    print(key)

'''
# 영단어 암기는 괴로워

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 (추가 시간 없음) | 1024 MB | 19583 | 8916 | 7059 | 45.175% |

## 문제

화은이는 이번 영어 시험에서 틀린 문제를 바탕으로 영어 단어 암기를 하려고 한다. 그 과정에서 효율적으로 영어 단어를 외우기 위해 영어 단어장을 만들려 하고 있다. 화은이가 만들고자 하는 단어장의 단어 순서는 다음과 같은 우선순위를 차례로 적용하여 만들어진다.

1. 자주 나오는 단어일수록 앞에 배치한다.
2. 해당 단어의 길이가 길수록 앞에 배치한다.
3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

𝑀$M$보다 짧은 길이의 단어의 경우 읽는 것만으로도 외울 수 있기 때문에 길이가 𝑀$M$이상인 단어들만 외운다고 한다. 화은이가 괴로운 영단어 암기를 효율적으로 할 수 있도록 단어장을 만들어 주자.

## 입력

첫째 줄에는 영어 지문에 나오는 단어의 개수 𝑁$N$과 외울 단어의 길이 기준이 되는 𝑀$M$이 공백으로 구분되어 주어진다. (1≤𝑁≤100000$1 \leq N \leq 100\,000$, 1≤𝑀≤10$1 \leq M \leq 10$)

둘째 줄부터 𝑁+1$N+1$번째 줄까지 외울 단어를 입력받는다. 이때의 입력은 알파벳 소문자로만 주어지며 단어의 길이는 10$10$을 넘지 않는다.

단어장에 단어가 반드시 1개 이상 존재하는 입력만 주어진다.

## 출력

화은이의 단어장에 들어 있는 단어를 단어장의 앞에 위치한 단어부터 한 줄에 한 단어씩 순서대로 출력한다.

## 예제 입력 1

```
7 4
apple
ant
sand
apple
append
sand
sand

```

## 예제 출력 1

```
sand
apple
append

```

## 예제 입력 2

```
12 5
appearance
append
attendance
swim
swift
swift
swift
mouse
wallet
mouse
ice
age

```

## 예제 출력 2

```
swift
mouse
appearance
attendance
append
wallet

```

## 노트

다음과 같이 사용하면 입출력을 좀 더 빠르게 사용할 수 있다.

- C++을 사용하고 있고 `cin/cout`을 사용하고자 한다면, `cin.tie(NULL)`과 `sync_with_stdio(false)`를 둘 다 적용해 주고, `endl` 대신 개행문자(`\n`)를 쓰자. 단, 이렇게 하면 더 이상 `scanf/printf/puts/getchar/putchar` 등 C의 입출력 방식을 사용하면 안 된다.
- Java를 사용하고 있다면, `Scanner`와 `System.out.println` 대신 `BufferedReader`와 `BufferedWriter`를 사용할 수 있다. `BufferedWriter.flush`는 맨 마지막에 한 번만 하면 된다.
- Python을 사용하고 있다면, `input` 대신 `sys.stdin.readline`을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 `.rstrip()`을 추가로 해 주는 것이 좋다. 마지막으로, Pypy3은 Python 3와 같은 문법을 가지면서 일반적으로 더 빠르게 동작한다. 연산량이 많은 문제에서 Python을 사용하고자 한다면 Pypy로 제출하는 것을 권장한다.

## 출처

[Camp](https://www.acmicpc.net/category/220) > [ICPC Sinchon Algorithm Camp](https://www.acmicpc.net/category/499) > [2021 ICPC Sinchon Winter Algorithm Camp Contest](https://www.acmicpc.net/category/795) > [초급](https://www.acmicpc.net/category/detail/2428) A번

- 문제를 검수한 사람: [gratus907](https://www.acmicpc.net/user/gratus907), [iknoom1107](https://www.acmicpc.net/user/iknoom1107), [jwvg0425](https://www.acmicpc.net/user/jwvg0425), [tony9402](https://www.acmicpc.net/user/tony9402)
- 문제를 만든 사람: [whaeun25](https://www.acmicpc.net/user/whaeun25)

## 알고리즘 분류

- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [문자열](https://www.acmicpc.net/problem/tag/158)
- [정렬](https://www.acmicpc.net/problem/tag/97)
- [해시를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/136)
- [트리를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/74)

## 메모

get으로 dictionary에서 불러오고 카운팅.

[Python dict key, value 추가 딕셔너리 원소 추가](https://www.notion.so/Python-dict-key-value-e1405c8ff17a46a19d2078eccb33cdda?pvs=21) 

길이 조건에 맞는 단어 중 많이 나온 개수, 단어 길이, 사전 순 정렬 후 출력.

[Python sorted](https://www.notion.so/Python-sorted-3e3e7bf211914292b7689300b265c556?pvs=21) 

[Python dict key value 변경, 정렬, 최대](https://www.notion.so/Python-dict-key-value-4aabbcb899e146a1901a82f14d36c927?pvs=21)
'''
