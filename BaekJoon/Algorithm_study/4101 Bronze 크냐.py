import sys


input = sys.stdin.readline
while True:
    a, b = map(int, input().strip().split())
    if a == 0 and b == 0:
        break

    if a > b:
        print('Yes')
    else:
        print('No')

'''
# 크냐? 다국어한국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 49512 | 24410 | 22594 | 50.347% |

## 문제

두 양의 정수가 주어졌을 때, 첫 번째 수가 두 번째 수보다 큰지 구하는 프로그램을 작성하시오.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 두 정수가 주어진다. 두 수는 백만보다 작거나 같은 양의 정수이다. 입력의 마지막 줄에는 0이 두 개 주어진다.

## 출력

각 테스트 케이스마다, 첫 번째 수가 두 번째 수보다 크면 Yes를, 아니면 No를 한 줄에 하나씩 출력한다.

## 예제 입력 1 복사

```
1 19
4 4
23 14
0 0

```

## 예제 출력 1 복사

```
No
No
Yes

```

## 출처

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [North America](https://www.acmicpc.net/category/8) > [Southeast USA Regional](https://www.acmicpc.net/category/40) > [2009 Southeast USA Regional Programming Contest](https://www.acmicpc.net/category/detail/179) PA번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 문제의 오타를 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)

## 메모
'''
