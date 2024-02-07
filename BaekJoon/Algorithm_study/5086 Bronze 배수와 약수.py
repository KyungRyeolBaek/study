import sys


input = sys.stdin.readline
value = input().strip()
while value != "0 0":
    A, B = map(int, value.split())
    if A == 0 or B == 0:
        break
    if B % A == 0:
        print("factor")
    elif A % B == 0:
        print("multiple")
    else:
        print("neither")
    value = input().strip()

'''
# 배수와 약수 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 51476 | 32472 | 29924 | 63.896% |

## 문제

4 × 3 = 12이다.

이 식을 통해 다음과 같은 사실을 알 수 있다.

3은 12의 약수이고, 12는 3의 배수이다.

4도 12의 약수이고, 12는 4의 배수이다.

두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.

1. 첫 번째 숫자가 두 번째 숫자의 약수이다.
2. 첫 번째 숫자가 두 번째 숫자의 배수이다.
3. 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.

## 입력

입력은 여러 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다. 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.

## 출력

각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.

## 예제 입력 1

```
8 16
32 4
17 5
0 0

```

## 예제 출력 1

```
factor
multiple
neither

```

## 출처

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [South Pacific](https://www.acmicpc.net/category/92) > [South Pacific Region](https://www.acmicpc.net/category/104) > [New Zealand Programming Contest](https://www.acmicpc.net/category/93) > [NZPC 2011](https://www.acmicpc.net/category/detail/446) A번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 문제의 오타를 찾은 사람: [he1fire](https://www.acmicpc.net/user/he1fire)
- 빠진 조건을 찾은 사람: [psu9808](https://www.acmicpc.net/user/psu9808)
- 잘못된 조건을 찾은 사람: [toysmars](https://www.acmicpc.net/user/toysmars)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [사칙연산](https://www.acmicpc.net/problem/tag/121)

## 메모
'''