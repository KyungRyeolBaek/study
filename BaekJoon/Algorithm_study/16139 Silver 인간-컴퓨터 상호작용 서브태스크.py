import sys


input = sys.stdin.readline
S = input().rstrip()
dict_S = {chr(s): [0] * (len(S) + 1) for s in range(97, 123)}
for i in range(len(S)):
    for char in dict_S:
        dict_S[char][i + 1] = dict_S[char][i]
    dict_S[S[i]][i + 1] += 1

N = int(input())
for _ in range(N):
    a, l, r = input().rstrip().split()
    l, r = map(int, [l, r])
    print(dict_S[a][r + 1] - dict_S[a][l])

'''
# 인간-컴퓨터 상호작용 서브태스크

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 (추가 시간 없음) | 256 MB | 24845 | 6843 | 5452 | 29.098% |

## 문제

승재는 인간-컴퓨터 상호작용에서 생체공학 설계를 공부하다가 키보드 자판이 실용적인지 궁금해졌다. 이를 알아보기 위해 승재는 다음과 같은 생각을 했다.

'문자열에서 특정 알파벳이 몇 번 나타나는지 알아봐서 자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인할 수 있을 것이다.'

승재를 도와 특정 문자열 S$S$, 특정 알파벳 α$\alpha$와 문자열의 구간 [l,r]$[l,r]$이 주어지면 S$S$의 l$l$번째 문자부터 r$r$번째 문자 사이에 α$\alpha$가 몇 번 나타나는지 구하는 프로그램을 작성하여라. 승재는 문자열의 문자는 0$0$번째부터 세며, l$l$번째와 r$r$번째 문자를 포함해서 생각한다. 주의할 점은 승재는 호기심이 많기에 (통계적으로 크게 무의미하지만) 같은 문자열을 두고 질문을 q$q$번 할 것이다.

## 입력

첫 줄에 문자열 S$S$가 주어진다. 문자열의 길이는 200,000$200,000$자 이하이며 알파벳 소문자로만 구성되었다. 두 번째 줄에는 질문의 수 q$q$가 주어지며, 문제의 수는 1≤q≤200,000$1\leq q\leq 200,000$을 만족한다. 세 번째 줄부터 (q+2)$(q+2)$번째 줄에는 질문이 주어진다. 각 질문은 알파벳 소문자 αi$\alpha_i$와 0≤li≤ri<|S|$0\leq l_i\leq r_i<|S|$를 만족하는 정수 li,ri$l_i,r_i$가 공백으로 구분되어 주어진다.

## 출력

각 질문마다 줄을 구분해 순서대로 답변한다. i$i$번째 줄에 S$S$의 li$l_i$번째 문자부터 ri$r_i$번째 문자 사이에 αi$\alpha_i$가 나타나는 횟수를 출력한다.

## 서브태스크 1 (50점)

문자열의 길이는 2,000$2,000$자 이하, 질문의 수는 2,000$2,000$개 이하이다.

## 서브태스크 2 (50점)

추가 제한 조건이 없다.

## 예제 입력 1

```
seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10
```

## 예제 출력 1

```
0
1
2
1
```

## 출처

[University](https://www.acmicpc.net/category/5) > [광주과학기술원](https://www.acmicpc.net/category/434) > [광주과학기술원 HOLICS 알고리즘 대회 2018](https://www.acmicpc.net/category/detail/1916) B번

- 문제를 만든 사람: [hwy16016](https://www.acmicpc.net/user/hwy16016)
- 문제의 오타를 찾은 사람: [shiftpsh](https://www.acmicpc.net/user/shiftpsh)

## 알고리즘 분류

- [누적 합](https://www.acmicpc.net/problem/tag/139)

## 채점 및 기타 정보

- 예제는 채점하지 않는다.

## 메모

그냥 풀면 50점

시간초과 걸림

문자열마다 dictionary에 넣어놓고 해당 해당 문자열의 위치에 따라서 누적합 계산.

누적합: 큰 값까지의 총합 - 작은 값까지의 총합 = 해당 범위의 합

python3로는 해결 안됨 pypy3로 해결해야함
'''