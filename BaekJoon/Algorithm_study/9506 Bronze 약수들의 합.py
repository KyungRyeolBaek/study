import sys


input = sys.stdin.readline
while True:
    f = 1
    f_list = []
    n = int(input())
    if n == -1:
        break

    while n:
        if n % f == 0:
            f_list.append(f)
        f += 1
        if f >= n:
            break

    if sum(f_list) == n:
        print(str(n), '=', ' + '.join([str(f) for f in f_list]))
    else:
        print(str(n), 'is NOT perfect.')

'''
# 약수들의 합 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 128 MB | 38098 | 19424 | 17379 | 51.839% |

## 문제

어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.

예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.

n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

## 입력

입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100,000)

입력의 마지막엔 -1이 주어진다.

## 출력

테스트케이스 마다 한줄에 하나씩 출력해야 한다.

n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).

이때, 약수들은 오름차순으로 나열해야 한다.

n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.

## 예제 입력 1

```
6
12
28
-1

```

## 예제 출력 1

```
6 = 1 + 2 + 3
12 is NOT perfect.
28 = 1 + 2 + 4 + 7 + 14

```

## 출처

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [North America](https://www.acmicpc.net/category/8) > [Pacific Northwest Regional](https://www.acmicpc.net/category/33) > [2013 Pacific Northwest Region Programming Contest](https://www.acmicpc.net/category/detail/1173) F번

- 문제의 오타를 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013), [pkcchoi3](https://www.acmicpc.net/user/pkcchoi3)
- 데이터를 추가한 사람: [seong954t](https://www.acmicpc.net/user/seong954t)
- 문제를 번역한 사람: [yukariko](https://www.acmicpc.net/user/yukariko)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)
- [정수론](https://www.acmicpc.net/problem/tag/95)

## 메모
'''