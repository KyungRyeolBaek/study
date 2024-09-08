import sys


input = sys.stdin.readline
a = input().strip()
b = input().strip()
if b in a:
    print('go')
else:
    print('no')

'''
# 아! 다국어한국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 24018 | 14755 | 13857 | 62.382% |

## 문제

재환이는 저스틴 비버 콘서트에서 소리를 너무 많이 질러서 인후염에 걸렸다.

의사는 재환이에게 "aaah"를 말해보라고 시켰다. 안타깝게도 재환이는 의사가 원하는만큼 소리를 길게 낼 수 없는 경우가 있었다.

각각의 의사는 재환이에게 특정한 길이의 "aah"를 말해보라고 요청한다. 어떤 의사는 "aaaaaah"를 요구하기도 하고, "h"만 요구하는 의사도 있다.

모든 의사는 자신이 원하는 길이의 "aah"를 듣지 못하면 진단을 내릴 수 없다.

따라서, 재환이는 집에서 자신이 얼마나 길게 "aah"를 낼 수 있는지 알아냈고, 자기가 소리낼 수 있는 길이의 "aah"를 요구하는 의사를 방문하려고 한다.

재환이가 낼 수 있는 "aah"의 길이와 의사가 요구하는 길이가 주어진다. 이때, 그 병원에 가야하는지 말아야하는지를 알아내는 프로그램을 작성하시오.

## 입력

입력은 두 줄로 이루어져 있다. 첫째 줄은 재환이가 가장 길게 낼 수 있는 "aaah"이다. 둘째 줄은 의사가 듣기를 원하는 "aah"이다. 두 문자열은 모두 a와 h로만 이루어져 있다. a의 개수는 0보다 크거나 같고, 999보다 작거나 같으며, 항상 h는 마지막에 하나만 주어진다.

## 출력

재환이가 그 병원에 가야하면 "go"를, 아니면 "no"를 출력한다.

## 예제 입력 1 복사

```
aaah
aaaaah

```

## 예제 출력 1 복사

```
no

```

## 예제 입력 2 복사

```
aaah
ah

```

## 예제 출력 2 복사

```
go

```

## 출처

!https://licensebuttons.net/l/by-sa/2.0/88x31.png

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [Europe](https://www.acmicpc.net/category/10) > [Northwestern European Regional Contest](https://www.acmicpc.net/category/15) > [Nordic Collegiate Programming Contest](https://www.acmicpc.net/category/46) > [NCPC 2012](https://www.acmicpc.net/category/detail/209) A번

- 문제의 오타를 찾은 사람: [79brue](https://www.acmicpc.net/user/79brue), [joonas](https://www.acmicpc.net/user/joonas)
- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)
- [문자열](https://www.acmicpc.net/problem/tag/158)

## 메모
'''
