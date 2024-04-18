import sys


input = sys.stdin.readline
N = int(input())
stay_members = {}
for _ in range(N):
    event = input().strip().split()
    if event[1] == 'enter':
        stay_members[event[0]] = True
    else:
        del stay_members[event[0]]

members = sorted(stay_members.keys(), reverse=True)
for member in members:
    print(member)

'''
# 회사에 있는 사람 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 53526 | 21985 | 16684 | 40.606% |

## 문제

상근이는 세계적인 소프트웨어 회사 기글에서 일한다. 이 회사의 가장 큰 특징은 자유로운 출퇴근 시간이다. 따라서, 직원들은 반드시 9시부터 6시까지 회사에 있지 않아도 된다.

각 직원은 자기가 원할 때 출근할 수 있고, 아무때나 퇴근할 수 있다.

상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다. (2 ≤ n ≤ 106) 다음 n개의 줄에는 출입 기록이 순서대로 주어지며, 각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다. "enter"인 경우는 출근, "leave"인 경우는 퇴근이다.

회사에는 동명이인이 없으며, 대소문자가 다른 경우에는 다른 이름이다. 사람들의 이름은 알파벳 대소문자로 구성된 5글자 이하의 문자열이다.

## 출력

현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.

## 예제 입력 1

```
4
Baha enter
Askar enter
Baha leave
Artem enter

```

## 예제 출력 1

```
Askar
Artem

```

## 출처

[Contest](https://www.acmicpc.net/category/45) > [KBTU Open](https://www.acmicpc.net/category/222) > [KBTU Open 2008](https://www.acmicpc.net/category/detail/938) E번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 빠진 조건을 찾은 사람: [haja](https://www.acmicpc.net/user/haja), [lyzqm](https://www.acmicpc.net/user/lyzqm)
- 데이터를 추가한 사람: [jh05013](https://www.acmicpc.net/user/jh05013)

## 알고리즘 분류

- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [해시를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/136)

## 메모

사전순 역순 정렬

dictionary 형태로 넣어야 뽑아올 때 빠름.

[길이가 같으면 사전 순으로](https://www.notion.so/dc55a92363a4440eb6f2fe78cbaaab7c?pvs=21)
'''