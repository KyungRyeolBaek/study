import sys


input = sys.stdin.readline
N = int(input().strip())
A = set(map(int, input().split()))
M = int(input().strip())
B = list(map(int, input().split()))

for b in B:
    if b in A:
        print(1)
    else:
        print(0)

'''
# 수 찾기

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 265061 | 82588 | 54727 | 30.116% |

## 문제

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

## 입력

첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

## 출력

M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

## 예제 입력 1

```
5
4 1 5 2 3
5
1 3 7 9 5

```

## 예제 출력 1

```
1
1
0
0
1

```

## 출처

- 데이터를 추가한 사람: [BaaaaaaaaaaarkingDog](https://www.acmicpc.net/user/BaaaaaaaaaaarkingDog), [djm03178](https://www.acmicpc.net/user/djm03178), [melthetensai](https://www.acmicpc.net/user/melthetensai)
- 문제의 오타를 찾은 사람: [bupjae](https://www.acmicpc.net/user/bupjae)
- 잘못된 데이터를 찾은 사람: [tncks0121](https://www.acmicpc.net/user/tncks0121)

## 알고리즘 분류

- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [정렬](https://www.acmicpc.net/problem/tag/97)
- [이분 탐색](https://www.acmicpc.net/problem/tag/12)

## 메모
'''
