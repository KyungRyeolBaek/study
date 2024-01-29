import sys


input = sys.stdin.readline
N, B = map(int, input().strip().split())
dic = {10 + idx: chr(i) for idx, i in enumerate(range(ord('A'), ord('Z') + 1))}
result = ''
while N:
    N, b = divmod(N, B)
    if b >= 10:
        b = dic[b]
    result += str(b)
print(result[::-1])

'''
# 진법 변환 2

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 0.5 초 (추가 시간 없음) | 256 MB | 42361 | 19892 | 17142 | 47.025% |

## 문제

10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

## 입력

첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

## 출력

첫째 줄에 10진법 수 N을 B진법으로 출력한다.

## 예제 입력 1

```
60466175 36

```

## 예제 출력 1

```
ZZZZZ

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [du9172](https://www.acmicpc.net/user/du9172)
- 문제의 오타를 찾은 사람: [zmtn94](https://www.acmicpc.net/user/zmtn94)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)

## 메모

아스키 코드 변환

[문자 -> 아스키코드 : ord()](https://www.notion.so/ord-c827be67a32341be98839480ea694e32?pvs=21) 

divmod 몫, 나머지 사용.

[몫과 나머지 구분 - divmod](https://www.notion.so/divmod-1149438fb762494bb9121ab5b2af3e97?pvs=21)
'''