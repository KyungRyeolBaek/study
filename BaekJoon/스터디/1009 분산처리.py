import sys


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    answer = ((a % 10) ** (b % 4 + 4)) % 10
    if answer == 0:
        print(10)
    else:
        print(answer)

'''
# 분산처리

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 102118 | 24083 | 19226 | 24.339% |

## 문제

재용이는 최신 컴퓨터 10대를 가지고 있다. 어느 날 재용이는 많은 데이터를 처리해야 될 일이 생겨서 각 컴퓨터에 1번부터 10번까지의 번호를 부여하고, 10대의 컴퓨터가 다음과 같은 방법으로 데이터들을 처리하기로 하였다.

1번 데이터는 1번 컴퓨터, 2번 데이터는 2번 컴퓨터, 3번 데이터는 3번 컴퓨터, ... ,

10번 데이터는 10번 컴퓨터, 11번 데이터는 1번 컴퓨터, 12번 데이터는 2번 컴퓨터, ...

총 데이터의 개수는 항상 ab개의 형태로 주어진다. 재용이는 문득 마지막 데이터가 처리될 컴퓨터의 번호가 궁금해졌다. 이를 수행해주는 프로그램을 작성하라.

## 입력

입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 정수 a와 b가 주어진다. (1 ≤ a < 100, 1 ≤ b < 1,000,000)

## 출력

각 테스트 케이스에 대해 마지막 데이터가 처리되는 컴퓨터의 번호를 출력한다.

## 예제 입력 1

```
5
1 6
3 7
6 2
7 100
9 635

```

## 예제 출력 1

```
1
7
6
1
9

```

## 출처

- 문제를 만든 사람: [hellodj](https://www.acmicpc.net/user/hellodj)
- 데이터를 추가한 사람: [kjiwhan0120](https://www.acmicpc.net/user/kjiwhan0120), [sait2000](https://www.acmicpc.net/user/sait2000)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)

## 메모

역대급으로 많이 틀렸다…

시간초과.. 시간이 오래 걸리는 문제는 아닌데 시간 제한을 타이트하게 준거 같다.

나머지를 이용해서 a의 일의 자리값만 구하고,

제곱하는 수인 b는 주기인 4로 나머지를 구해서 계산한다.

예외 상황인 b의 나머지가 0인 경우를 제외하기 위해 4를 더해주고,

10번째 컴퓨터의 값이 0이 나오지 않게 예외 처리가 필요하다.
'''