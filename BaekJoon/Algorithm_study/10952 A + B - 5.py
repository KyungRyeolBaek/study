import sys


input = sys.stdin.readline

while True:
    A, B = map(int, input().strip().split())
    if (A and B) != 0:
        print(A + B)
    else:
        break

'''
# A+B - 5

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 267980 | 140584 | 119678 | 52.277% |

## 문제

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

입력의 마지막에는 0 두 개가 들어온다.

## 출력

각 테스트 케이스마다 A+B를 출력한다.

## 예제 입력 1

```
1 1
2 3
3 4
9 8
5 2
0 0

```

## 예제 출력 1

```
2
5
7
17
7

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 빠진 조건을 찾은 사람: [djm03178](https://www.acmicpc.net/user/djm03178)
- 잘못된 조건을 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013)

## 비슷한 문제

- [1000번. A+B](https://www.acmicpc.net/problem/1000)
- [1001번. A-B](https://www.acmicpc.net/problem/1001)
- [1008번. A/B](https://www.acmicpc.net/problem/1008)
- [2558번. A+B - 2](https://www.acmicpc.net/problem/2558)
- [10950번. A+B - 3](https://www.acmicpc.net/problem/10950)
- [10951번. A+B - 4](https://www.acmicpc.net/problem/10951)
- [10953번. A+B - 6](https://www.acmicpc.net/problem/10953)
- [10998번. A×B](https://www.acmicpc.net/problem/10998)
- [11021번. A+B - 7](https://www.acmicpc.net/problem/11021)
- [11022번. A+B - 8](https://www.acmicpc.net/problem/11022)
- [15740번. A+B - 9](https://www.acmicpc.net/problem/15740)
- [15792번. A/B - 2](https://www.acmicpc.net/problem/15792)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)
- [사칙연산](https://www.acmicpc.net/problem/tag/121)

## 메모
'''
