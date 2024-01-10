import sys


input = sys.stdin.readline
A, B = map(int, input().split())

print(A / B)

'''
# A/B 스페셜 저지

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 128 MB | 656966 | 221989 | 185670 | 34.584% |

## 문제

두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

## 출력

첫째 줄에 A/B를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.

## 예제 입력 1

```
1 3

```

## 예제 출력 1

```
0.33333333333333333333333333333333

```

10-9 이하의 오차를 허용한다는 말은 꼭 소수 9번째 자리까지만 출력하라는 뜻이 아니다.

## 예제 입력 2

```
4 5

```

## 예제 출력 2

```
0.8

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 빠진 조건을 찾은 사람: [djm03178](https://www.acmicpc.net/user/djm03178)
- 내용을 추가한 사람: [jh05013](https://www.acmicpc.net/user/jh05013)

## 비슷한 문제

- [1000번. A+B](https://www.acmicpc.net/problem/1000)
- [1001번. A-B](https://www.acmicpc.net/problem/1001)
- [2558번. A+B - 2](https://www.acmicpc.net/problem/2558)
- [10950번. A+B - 3](https://www.acmicpc.net/problem/10950)
- [10951번. A+B - 4](https://www.acmicpc.net/problem/10951)
- [10952번. A+B - 5](https://www.acmicpc.net/problem/10952)
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