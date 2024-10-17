import sys


input = sys.stdin.readline
print(sum([int(input()) for _ in range(5)]))

'''
# 카드 게임 서브태스크다국어한국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 22887 | 18762 | 17715 | 82.935% |

## 문제

JOI군은 카드 게임을 하고 있다. 이 카드 게임은 5회의 게임으로 진행되며, 그 총점으로 승부를 하는 게임이다.

JOI군의 각 게임의 득점을 나타내는 정수가 주어졌을 때, JOI군의 총점을 구하는 프로그램을 작성하라.

## 입력

표준 입력에서 다음과 같은 데이터를 읽어온다.

- i 번째 줄(1 ≤ i ≤ 5)에는 정수 A가 적혀있다. 이것은 i번째 게임에서의 JOI군의 점수를 나타낸다.
    
    i
    

## 출력

표준 출력에 JOI군의 총점을 한 줄로 출력하라.

## 제한

- 0 ≤ A ≤ 100.
    
    i
    

## 서브태스크

| 번호 | 배점 | 제한 |
| --- | --- | --- |
| 1 | 20 | 0 ≤ Ai ≤ 10. |
| 2 | 80 | 추가적인 제약 조건이 없다. |

## 예제 입력 1 복사

```
1
2
3
4
5

```

## 예제 출력 1 복사

```
15

```

## 예제 입력 2 복사

```
0
100
0
10
100

```

## 예제 출력 2 복사

```
210

```

## 출처

!https://licensebuttons.net/l/by-sa/4.0/88x31.png

[Olympiad](https://www.acmicpc.net/category/2) > [Japanese Olympiad in Informatics](https://www.acmicpc.net/category/100) > [JOI 2012/2013](https://www.acmicpc.net/category/detail/542) P1번

[Olympiad](https://www.acmicpc.net/category/2) > [Japanese Olympiad in Informatics](https://www.acmicpc.net/category/100) > [JOI 2013/2014](https://www.acmicpc.net/category/detail/1249) P1번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon), [kyma123](https://www.acmicpc.net/user/kyma123)
- 데이터를 추가한 사람: [cubic](https://www.acmicpc.net/user/cubic)

## 알고리즘 분류

[보기](https://www.acmicpc.net/problem/5522#)

## 채점 및 기타 정보

- 예제는 채점하지 않는다.

## 메모
'''