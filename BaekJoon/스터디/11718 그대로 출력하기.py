import sys


input = sys.stdin.readline
while True:
    p = input().strip()
    if p == '':
        break
    else:
        print(p)

'''
# 그대로 출력하기

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 219904 | 65901 | 54527 | 32.669% |

## 문제

입력 받은 대로 출력하는 프로그램을 작성하시오.

## 입력

입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.

## 출력

입력받은 그대로 출력한다.

## 예제 입력 1

```
Hello
Baekjoon
Online Judge

```

## 예제 출력 1

```
Hello
Baekjoon
Online Judge

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)
- [문자열](https://www.acmicpc.net/problem/tag/158)

## 메모

빈 문자열 확인 방법. 

```python
string = ''
string.isspace()
```

뒤에 개행문자 strip으로 제거 해줘야 함.

input()은 빈 문자열 받으면 에러 문구 뜸.

sys.stdin.readline은 빈 문자열 받으면 ‘’로 출력.
'''
