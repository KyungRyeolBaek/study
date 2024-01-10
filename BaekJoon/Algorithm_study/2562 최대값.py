import sys


input = sys.stdin.readline
max_num = 0
index = 0
for i in range(9):
    num = int(input().strip())
    if num >= max_num:
        max_num = num
        index = i + 1
print(max_num)
print(index)

'''
# 최댓값

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 295574 | 136072 | 112745 | 45.527% |

## 문제

9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

## 입력

첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

## 출력

첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

## 예제 입력 1

```
3
29
38
12
57
74
40
85
61

```

## 예제 출력 1

```
85
8

```

## 출처

[Olympiad](https://www.acmicpc.net/category/2) > [한국정보올림피아드](https://www.acmicpc.net/category/55) > [한국정보올림피아드시․도지역본선](https://www.acmicpc.net/category/57) > [지역본선 2007](https://www.acmicpc.net/category/68) > [초등부](https://www.acmicpc.net/category/detail/361) 1번

- 데이터를 추가한 사람: [sait2000](https://www.acmicpc.net/user/sait2000)

## 알고리즘 분류

[보기](https://www.acmicpc.net/problem/2562#)

## 메모
'''