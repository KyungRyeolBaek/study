import sys


input = sys.stdin.readline
N = int(input())
have_cards = list(map(int, input().strip().split()))
cards_dict = {}
for card in have_cards:
    cards_dict[card] = cards_dict.get(card, 0) + 1

M = int(input())
find_cards = list(map(int, input().strip().split()))
result = []
for card in find_cards:
    result.append(str(cards_dict.get(card, 0)))

print(' '.join(result))

'''
# 숫자 카드 2

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 146408 | 56909 | 40590 | 37.508% |

## 문제

숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

## 출력

첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

## 예제 입력 1

```
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

```

## 예제 출력 1

```
3 0 0 1 2 0 0 2

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [bumsoo0515](https://www.acmicpc.net/user/bumsoo0515), [emppu](https://www.acmicpc.net/user/emppu), [jh05013](https://www.acmicpc.net/user/jh05013)
- 문제의 오타를 찾은 사람: [cko301](https://www.acmicpc.net/user/cko301), [mwy3055](https://www.acmicpc.net/user/mwy3055), [wkd48632](https://www.acmicpc.net/user/wkd48632)

## 알고리즘 분류

- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [정렬](https://www.acmicpc.net/problem/tag/97)
- [이분 탐색](https://www.acmicpc.net/problem/tag/12)
- [해시를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/136)

## 메모

dictionary에 저장해놓고 찾으면 빠르게 찾을 수 있음.

get 함수 사용. 값이 없으면 0 값이 있으면 그 값을 가져옴.

[Python dict key, value 추가 딕셔너리 원소 추가](https://www.notion.so/Python-dict-key-value-e1405c8ff17a46a19d2078eccb33cdda?pvs=21)
'''