import sys


input = sys.stdin.readline
N = int(input())
densers = set()
for _ in range(N):
    persons = input().strip().split()
    if len(densers) == 0:
        if 'ChongChong' in persons:
            for person in persons:
                densers.add(person)
    else:
        check = 0
        for person in persons:
            if person in densers:
                check = 1
        if check == 1:
            for person in persons:
                densers.add(person)
print(len(densers))

'''
# 붙임성 좋은 총총이

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 1024 MB | 9497 | 5955 | 5240 | 63.377% |

## 문제

https://upload.acmicpc.net/12d3d8d8-06c0-4b31-b661-0ce1bc935cf9/-/preview/

총총이는 친구 곰곰이의 소개로 **제2회 곰곰컵**에 출연할 기회를 얻었다!

총총이는 자신의 묘기인 **무지개 댄스**를 선보여, 여러분의 환심을 사려 한다. 이 댄스는 중독성이 강하기 때문에, 한번 보게 된 사람은 모두 따라 하게 돼버린다.

https://upload.acmicpc.net/4efdc327-804f-4929-8b6f-5b85577135c8/-/preview/

사람들이 만난 기록이 시간 순서대로 𝑁$N$개 주어진다. (총총이는 토끼이지만 이 문제에서는 편의상 사람이라고 가정한다.)

무지개 댄스를 추지 않고 있던 사람이 무지개 댄스를 추고 있던 사람을 만나게 된다면, 만난 시점 이후로 무지개 댄스를 추게 된다.

기록이 시작되기 이전 무지개 댄스를 추고 있는 사람은 총총이 뿐이라고 할 때, 마지막 기록 이후 무지개 댄스를 추는 사람이 몇 명인지 구해보자!

## 입력

첫번째 줄에는 사람들이 만난 기록의 수 𝑁 (1≤𝑁≤1 000)$N\ (1 \le N \le 1\ 000)$이 주어진다.

두번째 줄부터 𝑁$N$개의 줄에 걸쳐 사람들이 만난 기록이 주어진다. 𝑖+1$i + 1$번째 줄에는 𝑖$i$번째로 만난 사람들의 이름 𝐴𝑖$A_i$와 𝐵𝑖$B_i$가 공백을 사이에 두고 주어진다. 𝐴𝑖$A_i$와 𝐵𝑖$B_i$는 숫자와 영문 대소문자로 이루어진 최대 길이 20$20$의 문자열이며, 서로 같지 않다.

총총이의 이름은 `ChongChong`으로 주어지며, **기록에서 1회 이상 주어진다.**

동명이인은 없으며, 사람의 이름은 대소문자를 구분한다. (`ChongChong`과 `chongchong`은 다른 이름이다.)

## 출력

마지막 기록 이후 무지개 댄스를 추는 사람의 수를 출력하라.

## 예제 입력 1

```
12
bnb2011 chansol
chansol chogahui05
chogahui05 jthis
jthis ChongChong
jthis jyheo98
jyheo98 lms0806
lms0806 pichulia
pichulia pjshwa
pjshwa r4pidstart
r4pidstart swoon
swoon tony9402
tony9402 bnb2011

```

## 예제 출력 1

```
10

```

## 출처

[Contest](https://www.acmicpc.net/category/45) > [BOJ User Contest](https://www.acmicpc.net/category/984) > [곰곰컵](https://www.acmicpc.net/category/663) > [제2회 곰곰컵](https://www.acmicpc.net/category/detail/3232) B번

- 문제를 검수한 사람: [bnb2011](https://www.acmicpc.net/user/bnb2011), [chogahui05](https://www.acmicpc.net/user/chogahui05), [jthis](https://www.acmicpc.net/user/jthis), [jyheo98](https://www.acmicpc.net/user/jyheo98), [lms0806](https://www.acmicpc.net/user/lms0806), [pichulia](https://www.acmicpc.net/user/pichulia), [r4pidstart](https://www.acmicpc.net/user/r4pidstart), [tony9402](https://www.acmicpc.net/user/tony9402)
- 문제를 만든 사람: [pjshwa](https://www.acmicpc.net/user/pjshwa)

## 알고리즘 분류

- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [해시를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/136)
- [트리를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/74)

## 메모

ChongChong을 만났는데 춤추는 사람이 없으면 둘 다 춤추는 사람에 넣고, 그 뒤로 춤추는 사람과 만난 사람이 있으면 춤추는 사람에 추가.

set에 추가해서 같은 사람 제거.
'''
