import sys


input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().strip().split())

A = [[a, b], [d, e]]
B = [[c], [f]]
A_inv = [A_b / (a*e - b*d) for A_m in [[e, -b], [-d, a]] for A_b in A_m]
x = c * A_inv[0] + f * A_inv[1]
y = c * A_inv[2] + f * A_inv[3]
print(' '.join(list(map(lambda x: str(round(x)), [x, y]))))

'''
# 수학은 비대면강의입니다

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 (추가 시간 없음) | 1024 MB | 33331 | 16836 | 14866 | 51.236% |

## 문제

수현이는 4차 산업혁명 시대에 살고 있는 중학생이다. 코로나 19로 인해, 수현이는 버추얼 학교로 버추얼 출석해 버추얼 강의를 듣고 있다. 수현이의 버추얼 선생님은 문자가 2개인 연립방정식을 해결하는 방법에 대해 강의하고, 다음과 같은 문제를 숙제로 냈다.

다음 연립방정식에서 �$x$와 �$y$의 값을 계산하시오.{��+��=���+��=�\[\begin{cases}ax+by=c\\dx+ey=f\end{cases}\]

4차 산업혁명 시대에 숙제나 하고 앉아있는 것보다 버추얼 친구들을 만나러 가는 게 더 가치있는 일이라고 생각했던 수현이는 이런 연립방정식을 풀 시간이 없었다. 다행히도, 버추얼 강의의 숙제 제출은 인터넷 창의 빈 칸에 수들을 입력하는 식이다. 각 칸에는 −999$-999$ 이상 999$999$ 이하의 정수만 입력할 수 있다. 수현이가 버추얼 친구들을 만나러 버추얼 세계로 떠날 수 있게 도와주자.

## 입력

정수 �$a$, �$b$, �$c$, �$d$, �$e$, �$f$가 공백으로 구분되어 차례대로 주어진다. (−999≤�,�,�,�,�,�≤999$-999 \leq a,b,c,d,e,f \leq 999$)

문제에서 언급한 방정식을 만족하는 (�,�)$\left(x,y\right)$가 유일하게 존재하고, 이 때 �$x$와 �$y$가 각각 −999$-999$ 이상 999$999$ 이하의 정수인 경우만 입력으로 주어짐이 보장된다.

## 출력

문제의 답인 �$x$와 �$y$를 공백으로 구분해 출력한다.

## 예제 입력 1

```
1 3 -1 4 1 7

```

## 예제 출력 1

```
2 -1

```

## 예제 입력 2

```
2 5 8 3 -4 -11

```

## 예제 출력 2

```
-1 2

```

## 출처

[University](https://www.acmicpc.net/category/5) > [전국 대학생 프로그래밍 대회 동아리 연합](https://www.acmicpc.net/category/318) > [UCPC 2020 예선](https://www.acmicpc.net/category/detail/2270) A번

- 문제를 검수한 사람: [evenharder](https://www.acmicpc.net/user/evenharder), [jhnah917](https://www.acmicpc.net/user/jhnah917), [pichulia](https://www.acmicpc.net/user/pichulia), [sait2000](https://www.acmicpc.net/user/sait2000)
- 문제를 만든 사람: [shiftpsh](https://www.acmicpc.net/user/shiftpsh)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [브루트포스 알고리즘](https://www.acmicpc.net/problem/tag/125)

## 메모

역행렬 만들어서 코드 실행 해야함.

numpy 쓰면 모듈을 못찾는다는 오류가 남.

[Python 행렬](https://www.notion.so/Python-03fac016f814469f8ec87b3249585887?pvs=21)

```python
a*x + b*y = c
d*x + e*y = f

a, b * x = c
d, e   y   f
```
'''