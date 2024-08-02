import sys


input = sys.stdin.readline
N, K = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
num = sum(nums[:K])
max_num = num
for i in range(N - K):
    num -= nums[i]
    num += nums[i + K]
    if max_num < num:
        max_num = num

print(max_num)

'''
# 수열

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 61973 | 23104 | 17822 | 36.119% |

## 문제

매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.

예를 들어, 아래와 같이 10일 간의 온도가 주어졌을 때,

3 -2 -4 -9 0 3 7 13 8 -3

모든 연속적인 이틀간의 온도의 합은 아래와 같다.

https://upload.acmicpc.net/563b6bfd-12ff-4275-a869-90fdd43b6deb/-/preview/

이때, 온도의 합이 가장 큰 값은 21이다.

또 다른 예로 위와 같은 온도가 주어졌을 때, 모든 연속적인 5일 간의 온도의 합은 아래와 같으며,

https://upload.acmicpc.net/cb8d846c-2f90-475a-8901-1fb69de87397/-/preview/

이때, 온도의 합이 가장 큰 값은 31이다.

매일 측정한 온도가 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오.

## 입력

첫째 줄에는 두 개의 정수 N과 K가 한 개의 공백을 사이에 두고 순서대로 주어진다. 첫 번째 정수 N은 온도를 측정한 전체 날짜의 수이다. N은 2 이상 100,000 이하이다. 두 번째 정수 K는 합을 구하기 위한 연속적인 날짜의 수이다. K는 1과 N 사이의 정수이다. 둘째 줄에는 매일 측정한 온도를 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수들은 모두 -100 이상 100 이하이다.

## 출력

첫째 줄에는 입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력한다.

## 예제 입력 1

```
10 2
3 -2 -4 -9 0 3 7 13 8 -3

```

## 예제 출력 1

```
21

```

## 예제 입력 2

```
10 5
3 -2 -4 -9 0 3 7 13 8 -3

```

## 예제 출력 2

```
31

```

## 출처

[Olympiad](https://www.acmicpc.net/category/2) > [한국정보올림피아드](https://www.acmicpc.net/category/55) > [KOI 2011](https://www.acmicpc.net/category/59) > [초등부](https://www.acmicpc.net/category/detail/334) 1번

- 데이터를 추가한 사람: [jh05013](https://www.acmicpc.net/user/jh05013)
- 잘못된 데이터를 찾은 사람: [tncks0121](https://www.acmicpc.net/user/tncks0121)

## 알고리즘 분류

- [누적 합](https://www.acmicpc.net/problem/tag/139)
- [두 포인터](https://www.acmicpc.net/problem/tag/80)
- [슬라이딩 윈도우](https://www.acmicpc.net/problem/tag/68)

## 메모

구간별로 더해서 max_num이랑 비교

그냥 하면 시간 초과 뜸

한칸씩 움직이니 앞에 하나 빼고 마지막 값 하나 더하는 식으로  구간을 옮기면서 풀면 됨.
'''