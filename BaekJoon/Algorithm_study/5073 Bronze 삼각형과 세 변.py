import sys


input = sys.stdin.readline
triangle = 1
while True:
    triangle = sorted(list(map(int, input().strip().split())))
    if triangle == [0, 0, 0]:
        break
    if triangle[2] >= sum(triangle[0:2]):
        print('Invalid')
    else:
        count = len(set(triangle))
        print(['Equilateral', 'Isosceles', 'Scalene'][count - 1])

'''
# 삼각형과 세 변 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 31089 | 14724 | 13545 | 48.268% |

## 문제

삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.

- Equilateral : 세 변의 길이가 모두 같은 경우
- Isosceles : 두 변의 길이만 같은 경우
- Scalene : 세 변의 길이가 모두 다른 경우

단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다. 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.

세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.

## 입력

각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.

## 출력

각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.

## 예제 입력 1

```
7 7 7
6 5 4
3 2 5
6 2 6
0 0 0

```

## 예제 출력 1

```
Equilateral
Scalene
Invalid
Isosceles

```

## 출처

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [South Pacific](https://www.acmicpc.net/category/92) > [South Pacific Region](https://www.acmicpc.net/category/104) > [New Zealand Programming Contest](https://www.acmicpc.net/category/93) > [NZPC 2012](https://www.acmicpc.net/category/detail/445) B번

- 문제의 오타를 찾은 사람: [corea](https://www.acmicpc.net/user/corea), [lety](https://www.acmicpc.net/user/lety)
- 잘못된 번역을 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013)
- 문제를 번역한 사람: [john6014](https://www.acmicpc.net/user/john6014)
- 잘못된 데이터를 찾은 사람: [kookmin20103324](https://www.acmicpc.net/user/kookmin20103324)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)
- [기하학](https://www.acmicpc.net/problem/tag/100)

## 메모

삼각형의 조건

- 가장 긴 변 > 다른 두 변의 합

정삼각형 : Equilateral

이등변 삼각형 : Isosceles

삼각형 : Scalene
'''