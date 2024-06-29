import sys


def hanoi(n, from_pos, to_pos, aux_pos):
    global count, moves
    if n == 1:
        count += 1
        moves.append(f'{from_pos} {to_pos}')
        return count
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    count +=1
    moves.append(f'{from_pos} {to_pos}')
    hanoi(n - 1, aux_pos, to_pos, from_pos)
    return count


count = 0
moves = []
input = sys.stdin.readline
print(hanoi(int(input().strip()), 1, 3, 2))
for move in moves:
    print(move)

'''
# 하노이 탑 이동 순서

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 90844 | 46637 | 35455 | 50.858% |

## 문제

세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

1. 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
2. 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.

이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

아래 그림은 원판이 5개인 경우의 예시이다.

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11729/hanoi.png

## 입력

첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

## 출력

첫째 줄에 옮긴 횟수 K를 출력한다.

두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.

## 예제 입력 1

```
3

```

## 예제 출력 1

```
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 빠진 조건을 찾은 사람: [hayman42](https://www.acmicpc.net/user/hayman42)

## 알고리즘 분류

- [재귀](https://www.acmicpc.net/problem/tag/62)

## 메모

[하노이 탑](https://www.notion.so/64e92cb022f34d96b9c100297af29124?pvs=21) 

움직이는 부분에 global 로 변수 두고 하나씩 카운트 하면 됨.

1일 때도 반환 해줘야함.
'''
