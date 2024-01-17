word = list(open(0))
count = 0

for t in word[1:]:
    memo = []
    s = ''
    tf = 1
    for a in t:
        if a != s:
            if a not in memo:
                memo.append(a)
                s = a
            else:
                tf = 0

    if tf:
        count += 1

print(count)


'''
# 그룹 단어 체커 성공

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 128 MB | 150458 | 79285 | 65291 | 53.074% |

## 문제

그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

## 출력

첫째 줄에 그룹 단어의 개수를 출력한다.

## 예제 입력 1

```
3
happy
new
year

```

## 예제 출력 1

```
3
```

## 예제 입력 2

```
4
aba
abab
abcabc
a

```

## 예제 출력 2

```
1

```

## 예제 입력 3

```
5
ab
aa
aca
ba
bb

```

## 예제 출력 3

```
4

```

## 예제 입력 4

```
2
yzyzy
zyzyz

```

## 예제 출력 4

```
0

```

## 예제 입력 5

```
1
z

```

## 예제 출력 5

```
1

```

## 예제 입력 6

```
9
aaa
aaazbz
babb
aazz
azbz
aabbaa
abacc
aba
zzaz

```

## 예제 출력 6

```
2

```

## 출처

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [djm03178](https://www.acmicpc.net/user/djm03178), [jh05013](https://www.acmicpc.net/user/jh05013)
- 문제의 오타를 찾은 사람: [joonas](https://www.acmicpc.net/user/joonas)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)
- [문자열](https://www.acmicpc.net/problem/tag/158)

## 메모
'''