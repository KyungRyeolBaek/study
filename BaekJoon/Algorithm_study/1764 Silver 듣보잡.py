import sys


input =sys.stdin.readline
N, M = map(int, input().strip().split())
none_hear = {input().strip(): True for _ in range(N)}
none_see = {input().strip(): True for _ in range(M)}
none_hear_see = []
if len(none_hear) <= len(none_see):
    for person in none_hear:
        if none_see.get(person, False) == True:
            none_hear_see.append(person)
else:
    for person in none_see:
        if none_hear.get(person, False) == True:
            none_hear_see.append(person)

none_hear_see.sort()
print(len(none_hear_see))
for person in none_hear_see:
    print(person)

'''
# 듣보잡

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 256 MB | 107605 | 46309 | 36059 | 41.278% |

## 문제

김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

## 출력

듣보잡의 수와 그 명단을 사전순으로 출력한다.

## 예제 입력 1

```
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

```

## 예제 출력 1

```
2
baesangwook
ohhenrie

```

## 출처

- 문제를 만든 사람: [author5](https://www.acmicpc.net/user/author5)

## 알고리즘 분류

- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [문자열](https://www.acmicpc.net/problem/tag/158)
- [정렬](https://www.acmicpc.net/problem/tag/97)
- [해시를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/136)

## 메모

dictionary 형태로 get 으로 불러오면 빠르게 처리 할 수 있음.

마지막에 sort로 사전순 정렬까지 진행.

[Python dict key, value 추가 딕셔너리 원소 추가](https://www.notion.so/Python-dict-key-value-e1405c8ff17a46a19d2078eccb33cdda?pvs=21)

[Python sorted](https://www.notion.so/Python-sorted-3e3e7bf211914292b7689300b265c556?pvs=21)
'''