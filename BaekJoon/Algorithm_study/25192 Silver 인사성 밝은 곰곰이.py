import sys


input = sys.stdin.readline
N = int(input())
names = set()
count = 0
for _ in range(N):
    name = input().strip()
    if name != 'ENTER':
        names.add(name)
    else:
        count += len(names)
        names = set()
count += len(names)
print(count)

'''
# 인사성 밝은 곰곰이

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 1024 MB | 17474 | 7861 | 6632 | 46.780% |

## 문제

https://upload.acmicpc.net/cd52b787-5b7c-4857-b917-a95c10fe6ee9/-/preview/

알고리즘 입문방 오픈 채팅방에서는 새로운 분들이 입장을 할 때마다 곰곰티콘을 사용해 인사를 한다. 이를 본 문자열 킬러 임스는 채팅방의 기록을 수집해 그 중 곰곰티콘이 사용된 횟수를 구해 보기로 했다.

`ENTER`는 새로운 사람이 채팅방에 입장했음을 나타낸다. 그 외는 채팅을 입력한 유저의 닉네임을 나타낸다. 닉네임은 숫자 또는 영문 대소문자로 구성되어 있다.

새로운 사람이 입장한 이후 처음 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사를 한다. 그 외의 기록은 곰곰티콘을 쓰지 않은 평범한 채팅 기록이다.

채팅 기록 중 곰곰티콘이 사용된 횟수를 구해보자!

## 입력

첫 번째 줄에는 채팅방의 기록 수를 나타내는 정수 𝑁$N$ 이 주어진다. (1≤𝑁≤100000$1 \le N \le 100\,000$)

두 번째 줄부터 𝑁$N$ 개의 줄에 걸쳐 새로운 사람의 입장을 나타내는 `ENTER`, 혹은 채팅을 입력한 유저의 닉네임이 문자열로 주어진다. (문자열길이1≤문자열 길이≤20$1 \le \texttt{문자열 길이} \le 20$)

첫 번째 주어지는 문자열은 무조건 `ENTER`이다.

## 출력

채팅 기록 중 곰곰티콘이 사용된 횟수를 출력하시오.

## 예제 입력 1

```
9
ENTER
pjshwa
chansol
chogahui05
lms0806
pichulia
r4pidstart
swoon
tony9402

```

## 예제 출력 1

```
8

```

## 예제 입력 2

```
7
ENTER
pjshwa
chansol
chogahui05
ENTER
pjshwa
chansol

```

## 예제 출력 2

```
5

```

첫번째 새로운 사람이 들어온 뒤  `pjshwa`, `chansol`, `chogahui05`은 모두 곰곰티콘으로 인사했다.

두번째 새로운 사람이 들어온 뒤  `pjshwa`와 `chansol`은 다시 곰곰티콘으로 인사했다.

## 예제 입력 3

```
3
ENTER
lms0806
lms0806

```

## 예제 출력 3

```
1

```

`lms0806`은 새로운 사람이 들어왔으므로 처음은 곰곰티콘으로 인사하고, 그 뒤로는 일반 채팅을 했다.

## 출처

[Contest](https://www.acmicpc.net/category/45) > [BOJ User Contest](https://www.acmicpc.net/category/984) > [곰곰컵](https://www.acmicpc.net/category/663) > [제1회 곰곰컵](https://www.acmicpc.net/category/detail/3121) B번

- 문제를 검수한 사람: [chansol](https://www.acmicpc.net/user/chansol), [chogahui05](https://www.acmicpc.net/user/chogahui05), [pichulia](https://www.acmicpc.net/user/pichulia), [pjshwa](https://www.acmicpc.net/user/pjshwa), [r4pidstart](https://www.acmicpc.net/user/r4pidstart), [tony9402](https://www.acmicpc.net/user/tony9402)
- 문제를 만든 사람: [lms0806](https://www.acmicpc.net/user/lms0806)
- 데이터를 추가한 사람: [pichulia](https://www.acmicpc.net/user/pichulia)

## 알고리즘 분류

- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [해시를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/136)
- [트리를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/74)

## 메모

엔터 있을 때 숫자를 다시 세어 주면 된다.
'''
