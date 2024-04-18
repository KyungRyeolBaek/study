import sys


input = sys.stdin.readline
num = [i + 1 for i in range(30)]
for _ in range(28):
    num.remove(int(input().strip()))
for n in num:
    print(n)

'''
# 과제 안 내신 분..? 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 100305 | 52146 | 45627 | 52.161% |

## 문제

X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.

교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

## 입력

입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.

## 출력

출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

## 예제 입력 1

```
3
1
4
5
7
9
6
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30

```

## 예제 출력 1

```
2
8

```

## 예제 입력 2

```
9
30
6
12
10
20
21
11
7
5
28
4
18
29
17
19
27
13
16
26
14
23
22
15
3
1
24
25

```

## 예제 출력 2

```
2
8

```

## 출처

!https://licensebuttons.net/l/by-sa/4.0/88x31.png

[Olympiad](https://www.acmicpc.net/category/2) > [Japanese Olympiad in Informatics](https://www.acmicpc.net/category/100) > [Japanese Olympiad in Informatics Qualification Round](https://www.acmicpc.net/category/101) > [JOI 2007 예선](https://www.acmicpc.net/category/detail/555) 2번

- 문제를 번역한 사람: [egpaltair](https://www.acmicpc.net/user/egpaltair)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)

## 메모

pop으로 할 경우 리스트에서 요소를 뽑아낸 후 리스트의 갱신이 일어나지 않기에 오류가 발생한다.

따라서 pop 부분을 remove로 바꿔서 진행할 경우 해결 된다.
'''