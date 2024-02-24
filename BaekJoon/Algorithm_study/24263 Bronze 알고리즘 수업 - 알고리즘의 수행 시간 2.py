import sys


def MenOfPassion(N: int, count: int, degree: int) -> int:
    sum = 0
    degree += 1
    for i in range(1, N + 1):
        sum += i
        count += 1
    return sum, count, degree


input = sys.stdin.readline
_, count, degree = MenOfPassion(int(input().strip()), 0, 0)
print(count)
print(degree)

'''
# 알고리즘 수업 - 알고리즘의 수행 시간 2

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 512 MB | 13148 | 10408 | 10020 | 79.733% |

## 문제

오늘도 서준이는 알고리즘의 수행시간 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

입력의 크기 *n*이 주어지면 MenOfPassion 알고리즘 수행 시간을 예제 출력과 같은 방식으로 출력해보자.

MenOfPassion 알고리즘은 다음과 같다.

```
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
}
```

## 입력

첫째 줄에 입력의 크기 *n*(1 ≤ *n* ≤ 500,000)이 주어진다.

## 출력

첫째 줄에 코드1 의 수행 횟수를 출력한다.

둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

## 예제 입력 1

```
7

```

## 예제 출력 1

```
7
1

```

코드1 이 7회 수행되고 알고리즘의 수행 시간이 *n*에 비례한다.

## 출처

- 문제를 검수한 사람: [heeda0528](https://www.acmicpc.net/user/heeda0528), [jhnah917](https://www.acmicpc.net/user/jhnah917), [jthis](https://www.acmicpc.net/user/jthis), [tlsdydaud1](https://www.acmicpc.net/user/tlsdydaud1)
- 문제를 만든 사람: [MenOfPassion](https://www.acmicpc.net/user/MenOfPassion)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)
- [시뮬레이션](https://www.acmicpc.net/problem/tag/141)

## 메모

콘솔에서 n을 입력 받아 1 부터 n 까지의 합을 구하는 함수의 수행시간, 최고 차항의 계수를 출력하면 됨.

빅오 표기법

[빅오 표기법, 시간복잡도](https://www.notion.so/a5f2a1e8b5b748f6b82a50d97ecc2d28?pvs=21)
'''
