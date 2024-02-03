import sys


input = sys.stdin.readline
N = int(input().strip())
count = 1
N -= 1
while N > 0:
    N -= 6 * count
    count += 1

print(count)

'''
# 벌집

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 128 MB | 171102 | 77413 | 65896 | 44.787% |

## 문제

![https://www.acmicpc.net/JudgeOnline/upload/201009/3(2).png](https://www.acmicpc.net/JudgeOnline/upload/201009/3(2).png)

위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

## 입력

첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

## 출력

입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

## 예제 입력 1

```
13

```

## 예제 출력 1

```
3

```

## 출처

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [Asia Pacific](https://www.acmicpc.net/category/42) > [Korea](https://www.acmicpc.net/category/211) > [Nationwide Internet Competition](https://www.acmicpc.net/category/256) > [Seoul Nationalwide Internet Competition 2004](https://www.acmicpc.net/category/detail/1089) B번

- 문제의 오타를 찾은 사람: [waylight3](https://www.acmicpc.net/user/waylight3)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)

## 메모

```python
1 1
7 6
19 12
37 18
```
'''