import sys


def MenOfPassion(n, count=0, bigO=0):
    sum = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                sum += i * j * k
                count += 1
    bigO += 2
    return sum, count, bigO


input = sys.stdin.readline
n = int(input().strip())
count = sum([i * (i + 1) // 2 for i in range(1, n - 1)])
print(count)
print(3)

'''
# 알고리즘 수업 - 알고리즘의 수행 시간 6

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 512 MB | 17246 | 8475 | 8009 | 50.185% |

## 문제

오늘도 서준이는 알고리즘의 수행시간 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

입력의 크기 *n*이 주어지면 MenOfPassion 알고리즘 수행 시간을 예제 출력과 같은 방식으로 출력해보자.

MenOfPassion 알고리즘은 다음과 같다.

```
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
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
35
3

```

코드1 이 35회 수행되고 알고리즘의 수행 시간이 *n3*에 비례한다.

## 출처

- 문제를 검수한 사람: [heeda0528](https://www.acmicpc.net/user/heeda0528), [jhnah917](https://www.acmicpc.net/user/jhnah917), [jthis](https://www.acmicpc.net/user/jthis), [tlsdydaud1](https://www.acmicpc.net/user/tlsdydaud1)
- 문제를 만든 사람: [MenOfPassion](https://www.acmicpc.net/user/MenOfPassion)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)
- [시뮬레이션](https://www.acmicpc.net/problem/tag/141)

## 메모

시간 복잡도, 빅오 표기법

[빅오 표기법, 시간복잡도](https://www.notion.so/a5f2a1e8b5b748f6b82a50d97ecc2d28?pvs=21)
'''

