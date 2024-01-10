import sys


input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    count = 0
    x1, y1, x2, y2 = list(map(int, input().strip().split()))
    n = int(input().strip())
    C = [list(map(int, input().strip().split())) for _ in range(n)]

    for cx, cy, r in C:
        distance_1 = ((x1 - cx)**2 + (y1 - cy)**2)**0.5
        distance_2 = ((x2 - cx)**2 + (y2 - cy)**2)**0.5

        if r > distance_1 and r > distance_2:
            pass
        elif r > distance_1:
            count += 1
        elif r > distance_2:
            count += 1

    print(count)


'''
# 어린 왕자

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 128 MB | 38515 | 17245 | 14492 | 45.809% |

## 문제

어린 왕자는 소혹성 B-664에서 자신이 사랑하는 한 송이 장미를 위해 살아간다. 어느 날 장미가 위험에 빠지게 된 것을 알게 된 어린 왕자는, 장미를 구하기 위해 은하수를 따라 긴 여행을 하기 시작했다. 하지만 어린 왕자의 우주선은 그렇게 좋지 않아서 행성계 간의 이동을 최대한 피해서 여행해야 한다. 아래의 그림은 어린 왕자가 펼쳐본 은하수 지도의 일부이다.

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/upload/201003/dfcmhrjj_113gw6bcng2_b.gif

빨간 실선은 어린 왕자가 출발점에서 도착점까지 도달하는데 있어서 필요한 행성계 진입/이탈 횟수를 최소화하는 경로이며, 원은 행성계의 경계를 의미한다. 이러한 경로는 여러 개 존재할 수 있지만 적어도 3번의 행성계 진입/이탈이 필요하다는 것을 알 수 있다.

위와 같은 은하수 지도, 출발점, 도착점이 주어졌을 때 어린 왕자에게 필요한 최소의 행성계 진입/이탈 횟수를 구하는 프로그램을 작성해 보자. 행성계의 경계가 맞닿거나 서로 교차하는 경우는 없다. 또한, 출발점이나 도착점이 행성계 경계에 걸쳐진 경우 역시 입력으로 주어지지 않는다.

## 입력

입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트케이스에 대해 첫째 줄에 출발점 (x1, y1)과 도착점 (x2, y2)이 주어진다. 두 번째 줄에는 행성계의 개수 n이 주어지며, 세 번째 줄부터 n줄에 걸쳐 행성계의 중점과 반지름 (cx, cy, r)이 주어진다.

## 출력

각 테스트 케이스에 대해 어린 왕자가 거쳐야 할 최소의 행성계 진입/이탈 횟수를 출력한다.

## 제한

- 1000 ≤ x, y, x, y, c, c ≤ 1000
    
    1
    
    1
    
    2
    
    2
    
    x
    
    y
    
- 1 ≤ r ≤ 1000
- 1 ≤ n ≤ 50
- 좌표와 반지름은 모두 정수

## 예제 입력 1

```
2
-5 1 12 1
7
1 1 8
-3 -1 1
2 2 2
5 5 1
-4 5 1
12 1 1
12 1 2
-5 1 5 1
1
0 0 2

```

## 예제 출력 1

```
3
0

```

## 예제 입력 2

```
3
-5 1 5 1
3
0 0 2
-6 1 2
6 2 2
2 3 13 2
8
-3 -1 1
2 2 3
2 3 1
0 1 7
-4 5 1
12 1 1
12 1 2
12 1 3
102 16 19 -108
12
-107 175 135
-38 -115 42
140 23 70
148 -2 39
-198 -49 89
172 -151 39
-179 -52 43
148 42 150
176 0 10
153 68 120
-56 109 16
-187 -174 8

```

## 예제 출력 2

```
2
5
3

```

## 출처

- 문제를 번역한 사람: [AIAI](https://www.acmicpc.net/user/AIAI)
- 문제의 오타를 찾은 사람: [imgosari](https://www.acmicpc.net/user/imgosari), [jenny00513](https://www.acmicpc.net/user/jenny00513), [jh05013](https://www.acmicpc.net/user/jh05013), [lentti](https://www.acmicpc.net/user/lentti), [rdd6584](https://www.acmicpc.net/user/rdd6584)
- 잘못된 번역을 찾은 사람: [ntopia](https://www.acmicpc.net/user/ntopia)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [기하학](https://www.acmicpc.net/problem/tag/100)

## 메모

원이 서로 부딛히지 않기에 가능한 문제. 
원의 중점과 시작점 또는 끝점 간의 거리가 반지름보다 클 때만 카운트 추가. 
원의 중점과 시작점 그리고 끝점 간의 거리가 반지름보다 클 때는 원 안에서 선이 이어지기에 예외 처리.
'''
