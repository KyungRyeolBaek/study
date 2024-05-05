import sys
import math


input = sys.stdin.readline
N = int(input())
print(math.floor(N ** 0.5))

'''
# 창문 닫기

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 64 MB | 13184 | 6614 | 5847 | 50.392% |

## 문제

서강대학교 컴퓨터공학과 실습실 R912호에는 현재 N개의 창문이 있고 또 N명의 사람이 있다. 1번째 사람은 1의 배수 번째 창문을 열려 있으면 닫고 닫혀 있으면 연다.  2번째 사람은 2의 배수 번째 창문을 열려 있으면 닫고 닫혀 있으면 연다. 이러한 행동을 N번째 사람까지 진행한 후 열려 있는 창문의 개수를 구하라. 단, 처음에 모든 창문은 닫혀 있다.

예를 들어 현재 3개의 창문이 있고 3명의 사람이 있을 때,

1. 1번째 사람은 1의 배수인 1,2,3번 창문을 연다. (1, 1, 1)
2. 2번째 사람은 2의 배수인 2번 창문을 닫는다. (1, 0, 1)
3. 3번째 사람은 3의 배수인 3번 창문을 닫는다. (1, 0, 0)

결과적으로 마지막에 열려 있는 창문의 개수는 1개 이다.

## 입력

첫 번째 줄에는 창문의 개수와 사람의 수 N(**1 ≤ N ≤ 2,100,000,000**)이 주어진다.

## 출력

마지막에 열려 있는 창문의 개수를 출력한다.

## 예제 입력 1

```
3

```

## 예제 출력 1

```
1

```

## 예제 입력 2

```
24

```

## 예제 출력 2

```
4

```

## 출처

[University](https://www.acmicpc.net/category/5) > [서강대학교](https://www.acmicpc.net/category/83) > [2016 Sogang Programming Contest](https://www.acmicpc.net/category/690) > [Master](https://www.acmicpc.net/category/detail/1577) B번

- 문제의 오타를 찾은 사람: [jaehoo1](https://www.acmicpc.net/user/jaehoo1)
- 문제를 만든 사람: [jerryya211](https://www.acmicpc.net/user/jerryya211)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [정수론](https://www.acmicpc.net/problem/tag/95)

## 메모

제곱수일 때만 창문의 개수가 1개씩 늘어난다.

내림을 이용.

[Python 반올림, 내림, 올림](https://www.notion.so/Python-3064dbd4fa394d0cbab2c896391ca802?pvs=21)
'''