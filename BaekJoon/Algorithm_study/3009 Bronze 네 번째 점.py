import sys


input = sys.stdin.readline
point = []
for i in range(3):
    x, y = map(int, input().strip().split())
    point.append((x, y))
result = []
for i in range(2):
    if point[0][i] == point[1][i]:
        result.append(str(point[2][i]))
    elif point[0][i] == point[2][i]:
        result.append(str(point[1][i]))
    else:
        result.append(str(point[0][i]))

print(' '.join(result))

'''
# 네 번째 점 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 54345 | 39463 | 35374 | 73.511% |

## 문제

세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

## 입력

세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

## 출력

직사각형의 네 번째 점의 좌표를 출력한다.

## 예제 입력 1

```
5 5
5 7
7 5

```

## 예제 출력 1

```
7 7

```

## 예제 입력 2

```
30 20
10 10
10 20

```

## 예제 출력 2

```
30 10

```

## 출처

[Contest](https://www.acmicpc.net/category/45) > [Croatian Open Competition in Informatics](https://www.acmicpc.net/category/17) > [COCI 2007/2008](https://www.acmicpc.net/category/23) > [Contest #1](https://www.acmicpc.net/category/detail/100) 1번

[University](https://www.acmicpc.net/category/5) > [전국 대학생 프로그래밍 대회 동아리 연합](https://www.acmicpc.net/category/318) > [UCPC 2011](https://www.acmicpc.net/category/detail/3621) A번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 문제의 오타를 찾은 사람: [onjo0127](https://www.acmicpc.net/user/onjo0127)
- 데이터를 추가한 사람: [pichulia](https://www.acmicpc.net/user/pichulia)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)
- [기하학](https://www.acmicpc.net/problem/tag/100)

## 메모

x, y 위치의 동일한 값은 제외하고 다른 값들만 모으면 사각형의 마지막 점.
'''