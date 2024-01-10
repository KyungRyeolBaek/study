import sys


input = sys.stdin.readline
num_list = []
for _ in range(10):
    num = int(input().strip()) % 42
    if num not in num_list:
        num_list.append(num)

print(len(num_list))

'''
# 나머지 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 198710 | 114560 | 95498 | 57.638% |

## 문제

두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

## 출력

첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

## 예제 입력 1

```
1
2
3
4
5
6
7
8
9
10

```

## 예제 출력 1

```
10

```

각 수를 42로 나눈 나머지는 1, 2, 3, 4, 5, 6, 7, 8, 9, 10이다.

## 예제 입력 2

```
42
84
252
420
840
126
42
84
420
126

```

## 예제 출력 2

```
1

```

모든 수를 42로 나눈 나머지는 0이다.

## 예제 입력 3

```
39
40
41
42
43
44
82
83
84
85

```

## 예제 출력 3

```
6

```

각 수를 42로 나눈 나머지는 39, 40, 41, 0, 1, 2, 40, 41, 0, 1이다. 서로 다른 값은 6개가 있다.

## 출처

[Contest](https://www.acmicpc.net/category/45) > [Croatian Open Competition in Informatics](https://www.acmicpc.net/category/17) > [COCI 2006/2007](https://www.acmicpc.net/category/24) > [Contest #1](https://www.acmicpc.net/category/detail/108) 1번

- 데이터를 추가한 사람: [adfsfsf](https://www.acmicpc.net/user/adfsfsf)
- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [사칙연산](https://www.acmicpc.net/problem/tag/121)

## 메모
'''