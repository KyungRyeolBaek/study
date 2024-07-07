import sys


def stars(star, start, end):
    if start > end:
        return star

    triple_star = ''
    mid_star = ''
    for line in star.split('\n'):
        triple_star += line * 3 + '\n'
        mid_star += line + (len(line) * ' ') + line + '\n'
    
    return_star = triple_star + mid_star + triple_star.rstrip()
    return stars(return_star, start + 1, end)


input = sys.stdin.readline
N = int(input().strip())
n = 1
while True:
    if 3 ** n >= N:
        break
    else:
        n += 1
star = stars('*', 1, n)
print(star)

'''
# 별 찍기 - 10

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 76493 | 42652 | 31810 | 55.604% |

## 문제

재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

```
***
* *
***
```

N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

## 입력

첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

## 출력

첫째 줄부터 N번째 줄까지 별을 출력한다.

## 예제 입력 1

```
27

```

## 예제 출력 1

```
***************************
* ** ** ** ** ** ** ** ** *
***************************
***   ******   ******   ***
* *   * ** *   * ** *   * *
***   ******   ******   ***
***************************
* ** ** ** ** ** ** ** ** *
***************************
*********         *********
* ** ** *         * ** ** *
*********         *********
***   ***         ***   ***
* *   * *         * *   * *
***   ***         ***   ***
*********         *********
* ** ** *         * ** ** *
*********         *********
***************************
* ** ** ** ** ** ** ** ** *
***************************
***   ******   ******   ***
* *   * ** *   * ** *   * *
***   ******   ******   ***
***************************
* ** ** ** ** ** ** ** ** *
***************************

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 문제를 다시 작성한 사람: [jh05013](https://www.acmicpc.net/user/jh05013)

### 풀이

재귀 함수로 풀이

[별 찍기](https://www.notion.so/5bb5100fa9b04befaf50940d0cb0247c?pvs=21)
'''
