import sys


input = sys.stdin.readline

N = int(input().strip())
print((N // 4) * 'long ' + 'int')
'''
# 코딩은 체육과목 입니다

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 0.5 초 (추가 시간 없음) | 1024 MB (추가 메모리 없음) | 59967 | 38677 | 35291 | 65.176% |

## 문제

!https://u.acmicpc.net/ccbbee06-7e6f-4e56-bb9f-9a1abd795508/long-long-long-img1.png

오늘은 혜아의 면접 날이다. 면접 준비를 열심히 해서 앞선 질문들을 잘 대답한 혜아는 이제 마지막으로 칠판에 직접 코딩하는 문제를 받았다. 혜아가 받은 문제는 두 수를 더하는 문제였다. C++ 책을 열심히 읽었던 혜아는 간단히 두 수를 더하는 코드를 칠판에 적었다. 코드를 본 면접관은 다음 질문을 했다. “만약, 입출력이 �$N$바이트 크기의 정수라면 프로그램을 어떻게 구현해야 할까요?”

혜아는 책에 있는 정수 자료형과 관련된 내용을 기억해 냈다. 책에는 `long int`는 4$4$바이트 정수까지 저장할 수 있는 정수 자료형이고 `long long int`는 8$8$바이트 정수까지 저장할 수 있는 정수 자료형이라고 적혀 있었다. 혜아는 이런 생각이 들었다. “`int` 앞에 `long`을 하나씩 더 붙일 때마다 4$4$바이트씩 저장할 수 있는 공간이 늘어나는 걸까? 분명 `long long long int`는 12$12$바이트, `long long long long int`는 16$16$바이트까지 저장할 수 있는 정수 자료형일 거야!” 그렇게 혜아는 당황하는 면접관의 얼굴을 뒤로한 채 칠판에 정수 자료형을 써 내려가기 시작했다.

혜아가 �$N$바이트 정수까지 저장할 수 있다고 생각해서 칠판에 쓴 정수 자료형의 이름은 무엇일까?

## 입력

첫 번째 줄에는 문제의 정수 �$N$이 주어진다. (4≤�≤1000$(4\le N\le 1\, 000$; �$N$은 4$4$의 배수)$)$

## 출력

혜아가 �$N$바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.

## 예제 입력 1

```
4

```

## 예제 출력 1

```
long int

```

## 예제 입력 2

```
20

```

## 예제 출력 2

```
long long long long long int

```

## 노트

출력에서 `long`과 `long`, `long`과 `int` 사이에는 공백이 하나씩 들어간다.

실제로 C++에서 각 정수 자료형이 저장할 수 있는 수의 크기는 환경에 따라 달라질 수 있다. 덧붙여, 실제로 문제 내용과 같이 `long long long int`와 같은 자료형을 사용한 코드를 GCC의 C++ 컴파일러를 사용해 컴파일하려고 할 경우 `'long long long' is too long for GCC`라는 에러 메시지와 함께 컴파일되지 않는다.

## 출처

[University](https://www.acmicpc.net/category/5) > [전국 대학생 프로그래밍 대회 동아리 연합](https://www.acmicpc.net/category/318) > [UCPC 2022 예선](https://www.acmicpc.net/category/detail/3138) A번

- 문제를 만든 사람: [ho94949](https://www.acmicpc.net/user/ho94949)
- 문제를 검수한 사람: [shiftpsh](https://www.acmicpc.net/user/shiftpsh), [quickn](https://www.acmicpc.net/user/quickn), [myungwoo](https://www.acmicpc.net/user/myungwoo), [man_of_learning](https://www.acmicpc.net/user/man_of_learning), [lky7674](https://www.acmicpc.net/user/lky7674), [kclee2172](https://www.acmicpc.net/user/kclee2172), [jh05013](https://www.acmicpc.net/user/jh05013), [hyperbolic](https://www.acmicpc.net/user/hyperbolic), [99asdfg](https://www.acmicpc.net/user/99asdfg), [heeda0528](https://www.acmicpc.net/user/heeda0528), [functionx](https://www.acmicpc.net/user/functionx), [exqt](https://www.acmicpc.net/user/exqt), [doju](https://www.acmicpc.net/user/doju), [djm03178](https://www.acmicpc.net/user/djm03178), [bnb2011](https://www.acmicpc.net/user/bnb2011), [amok](https://www.acmicpc.net/user/amok)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)

## 메모
'''