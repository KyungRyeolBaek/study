import sys
import math


imput = sys.stdin.readline
A, B, V = map(int, input().strip().split())
day = (V - B) / (A - B)
print(math.ceil(day))

'''
# 달팽이는 올라가고 싶다

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 0.25 초 (추가 시간 없음) | 128 MB | 241661 | 76703 | 60750 | 31.179% |

## 문제

땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

## 출력

첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

## 예제 입력 1

```
2 1 5

```

## 예제 출력 1

```
4

```

## 예제 입력 2

```
5 1 6

```

## 예제 출력 2

```
2

```

## 예제 입력 3

```
100 99 1000000000

```

## 예제 출력 3

```
999999901

```

## 출처

[Contest](https://www.acmicpc.net/category/45) > [Croatian Open Competition in Informatics](https://www.acmicpc.net/category/17) > [COCI 2010/2011](https://www.acmicpc.net/category/20) > [Contest #2](https://www.acmicpc.net/category/detail/76) 1번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [CHULMING](https://www.acmicpc.net/user/CHULMING), [jm0707](https://www.acmicpc.net/user/jm0707), [tong39](https://www.acmicpc.net/user/tong39)
- 문제의 오타를 찾은 사람: [hellogaon](https://www.acmicpc.net/user/hellogaon)
- 빠진 조건을 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)

## 메모

[Python 반올림, 내림, 올림](https://www.notion.so/Python-3064dbd4fa394d0cbab2c896391ca802?pvs=21)
'''
