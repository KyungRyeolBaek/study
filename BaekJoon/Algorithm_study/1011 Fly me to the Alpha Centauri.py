'''
1 부터 시작해서 k + 1이 최대로 갈 수 있는 횟수를 구하면.
경우에 따라서 남은 값 처리 하면 될듯.
*1 : 1 : 1
2 : 11 : 2
3 : 111 : 3
*4 : 121 : 3
5 : 1211 : 4
6 : 1221 : 4
7 : 12211 : 5
8 : 12221 : 5
*9 : 12321 : 5
10 : 123211 : 6
11 : 123221 : 6
12 : 123321 : 6
13 : 1233211 : 7
14 : 1233221 : 7
15 : 1233321 : 7
*16 : 1234321 : 7
17 : 12343211 : 8
18 : 12343221 : 8
19 : 12343321 : 8
20 : 12344321 : 8
21 : 123443211 : 9
22 : 123443221 : 9
23 : 123443321 : 9
24 : 123444321 : 9
25 : 123454321 : 9


제곱근 일 때 12321 같은 수가 대칭을 이뤄서 다음 수부터는 글자수가 늘어남.
v = y - x
h_V = int(v ** 0.5)
제곱근 일 때 : h_v + h_v - 1
그 이상 일 때 :
만약 h_v >= (v - h_v)이면,
    h_v + h_v
그 외,
    h_v + h_v + 1
'''
import sys


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int, input().strip().split())
    v = y - x
    h_v = int(v ** 0.5)
    if v == h_v**2:
        print(2 * h_v - 1)
    elif (v - h_v**2) <= h_v:
        print(2 * h_v)
    else:
        print(2 * h_v + 1)

'''
# Fly me to the Alpha Centauri 성공

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 512 MB | 93866 | 28528 | 22383 | 31.424% |

## 문제

우현이는 어린 시절, 지구 외의 다른 행성에서도 인류들이 살아갈 수 있는 미래가 오리라 믿었다. 그리고 그가 지구라는 세상에 발을 내려 놓은 지 23년이 지난 지금, 세계 최연소 ASNA 우주 비행사가 되어 새로운 세계에 발을 내려 놓는 영광의 순간을 기다리고 있다.

그가 탑승하게 될 우주선은 Alpha Centauri라는 새로운 인류의 보금자리를 개척하기 위한 대규모 생활 유지 시스템을 탑재하고 있기 때문에, 그 크기와 질량이 엄청난 이유로 최신기술력을 총 동원하여 개발한 공간이동 장치를 탑재하였다. 하지만 이 공간이동 장치는 이동 거리를 급격하게 늘릴 경우 기계에 심각한 결함이 발생하는 단점이 있어서, 이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다. 예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나 사실상 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1 광년을 이동할 수 있으며, 그 다음에는 0 , 1 , 2 광년을 이동할 수 있는 것이다. ( 여기서 다시 2광년을 이동한다면 다음 시기엔 1, 2, 3 광년을 이동할 수 있다. )

!https://www.acmicpc.net/upload/201003/rlaehdgur.JPG

김우현은 공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 최소한의 작동 횟수로 이동하려 한다. 하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.

김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램을 작성하라.

## 입력

입력의 첫 줄에는 테스트케이스의 개수 T가 주어진다. 각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며, x는 항상 y보다 작은 값을 갖는다. (0 ≤ x < y < 231)

## 출력

각 테스트 케이스에 대해 x지점으로부터 y지점까지 정확히 도달하는데 필요한 최소한의 공간이동 장치 작동 횟수를 출력한다.

## 예제 입력 1

```
3
0 3
1 5
45 50

```

## 예제 출력 1

```
3
3
4

```

## 출처

- 문제를 번역한 사람: [AIAI](https://www.acmicpc.net/user/AIAI)
- 데이터를 추가한 사람: [iizuna](https://www.acmicpc.net/user/iizuna)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)

## 메모

1 부터 시작해서 k + 1이 최대로 갈 수 있는 횟수를 구하면.
경우에 따라서 남은 값 처리 하면 될듯.

| 1 | 1 | 1 |
| --- | --- | --- |
| 2 | 11 | 2 |
| 3 | 111 | 3 |
| 4 | 121 | 3 |
| 5 | 1211 | 4 |
| 6 | 1221 | 4 |
| 7 | 12211 | 5 |
| 8 | 12221 | 5 |
| 9 | 12321 | 5 |
| 10 | 123211 | 6 |
| 11 | 123221 | 6 |
| 12 | 123321 | 6 |
| 13 | 1233211 | 7 |
| 14 | 1233221 | 7 |
| 15 | 1233321 | 7 |
| 16 | 1234321 | 7 |
| 17 | 12343211 | 8 |
| 18 | 12343221 | 8 |
| 19 | 12343321 | 8 |
| 20 | 12344321 | 8 |
| 21 | 123443211 | 9 |
| 22 | 123443221 | 9 |
| 23 | 123443321 | 9 |
| 24 | 123444321 | 9 |
| 25 | 123454321 | 9 |
| 26 | 1234543211 | 10 |

제곱근 일 때 12321 같은 수가 대칭을 이뤄서 다음 수부터는 글자수가 늘어남.

```python
# 수도 코드
v = y - x
h_V = int(v ** 0.5)
제곱근 일 때 : h_v + h_v - 1
그 이상 일 때 :
만약 h_v >= (v - h_v)이면,
    h_v + h_v
그 외,
    h_v + h_v + 1
```
'''