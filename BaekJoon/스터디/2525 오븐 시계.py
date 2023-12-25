import sys


input = sys.stdin.readline

A, B = map(int, input().strip().split())
C = int(input().strip())

hour, minute = divmod((B + C), 60)
end_hour = (A + hour) % 24
print(end_hour, minute)

'''
# 오븐 시계 성공

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 247758 | 94993 | 80741 | 38.327% |

## 문제

KOI 전자에서는 건강에 좋고 맛있는 훈제오리구이 요리를 간편하게 만드는 인공지능 오븐을 개발하려고 한다. 인공지능 오븐을 사용하는 방법은 적당한 양의 오리 훈제 재료를 인공지능 오븐에 넣으면 된다. 그러면 인공지능 오븐은 오븐구이가 끝나는 시간을 분 단위로 자동적으로 계산한다.

또한, KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이 요리가 끝나는 시각을 알려 주는 디지털 시계가 있다.

훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

## 입력

첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.

## 출력

첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다. (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다. 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)

## 예제 입력 1

```
14 30
20

```

## 예제 출력 1

```
14 50

```

## 예제 입력 2

```
17 40
80

```

## 예제 출력 2

```
19 0

```

## 예제 입력 3

```
23 48
25

```

## 예제 출력 3

```
0 13

```

## 출처

[Olympiad](https://www.acmicpc.net/category/2) > [한국정보올림피아드](https://www.acmicpc.net/category/55) > [한국정보올림피아드시․도지역본선](https://www.acmicpc.net/category/57) > [지역본선 2012](https://www.acmicpc.net/category/58) > [초등부](https://www.acmicpc.net/category/detail/331) 1번

- 문제의 오타를 찾은 사람: [alkyne](https://www.acmicpc.net/user/alkyne)
- 데이터를 추가한 사람: [blast](https://www.acmicpc.net/user/blast), [ckd1675](https://www.acmicpc.net/user/ckd1675), [sunddjn](https://www.acmicpc.net/user/sunddjn)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [사칙연산](https://www.acmicpc.net/problem/tag/121)

## 메모

[몫과 나머지 구분 - divmod](https://www.notion.so/divmod-1149438fb762494bb9121ab5b2af3e97?pvs=21)
'''
