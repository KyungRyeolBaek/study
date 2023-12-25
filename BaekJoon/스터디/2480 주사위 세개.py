import sys


input = sys.stdin.readline
numbers = list(map(int, input().strip().split()))

big = 0
count = {}
for number in numbers:
    if number > big:
        big = number
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

same_number = max(count, key=count.get)
if len(count) == 1:
    print(10000 + same_number * 1000)
elif len(count) == 2:
    print(1000 + same_number * 100)
else:
    print(big * 100)

'''
# 주사위 세개

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 197003 | 92680 | 78870 | 47.215% |

## 문제

1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

## 입력

첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

## 출력

첫째 줄에 게임의 상금을 출력 한다.

## 예제 입력 1

```
3 3 6

```

## 예제 출력 1

```
1300

```

## 예제 입력 2

```
2 2 2

```

## 예제 출력 2

```
12000

```

## 예제 입력 3

```
6 2 5

```

## 예제 출력 3

```
600

```

## 출처

[Olympiad](https://www.acmicpc.net/category/2) > [한국정보올림피아드](https://www.acmicpc.net/category/55) > [한국정보올림피아드시․도지역본선](https://www.acmicpc.net/category/57) > [지역본선 2010](https://www.acmicpc.net/category/62) > [중등부](https://www.acmicpc.net/category/detail/344) 1번

- 데이터를 추가한 사람: [aname](https://www.acmicpc.net/user/aname), [tkdring3](https://www.acmicpc.net/user/tkdring3)
- 잘못된 데이터를 찾은 사람: [sait2000](https://www.acmicpc.net/user/sait2000)

## 알고리즘 분류

[보기](https://www.acmicpc.net/problem/2480#)

## 메모

max(dic,key=dic.get) # di.get 이용 여러개일 경우 맨앞 하나

[최대 value에 대한 key](https://www.notion.so/value-key-37777d75bbb94490a091a083417acd7b?pvs=21)
'''