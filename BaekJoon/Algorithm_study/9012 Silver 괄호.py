import sys


def is_balenced(string):
    stack = []
    parenthesis_string = {')': '('}
    
    for char in string:
        p_s_keys = parenthesis_string.keys()
        p_s_values = parenthesis_string.values()
        if char in p_s_keys:
            if not stack or parenthesis_string[char] != stack.pop():
                return 'NO'
        elif char in p_s_values:
            stack.append(char)
    if stack:
        return 'NO'
    else:
        return 'YES'


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    string = input().strip()
    print(is_balenced(string))

'''
# 괄호 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 210885 | 99600 | 71457 | 46.000% |

## 문제

괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.

## 입력

입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.

## 출력

출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.

## 예제 입력 1

```
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

```

## 예제 출력 1

```
NO
NO
YES
NO
YES
NO

```

## 예제 입력 2

```
3
((
))
())(()

```

## 예제 출력 2

```
NO
NO
NO

```

## 출처

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [Asia Pacific](https://www.acmicpc.net/category/42) > [Korea](https://www.acmicpc.net/category/211) > [Nationwide Internet Competition](https://www.acmicpc.net/category/256) > [Daejeon Nationalwide Internet Competition 2012](https://www.acmicpc.net/category/detail/1081) G번

- 데이터를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [jh05013](https://www.acmicpc.net/user/jh05013)
- 문제의 오타를 찾은 사람: [marona](https://www.acmicpc.net/user/marona)

## 알고리즘 분류

- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [문자열](https://www.acmicpc.net/problem/tag/158)
- [스택](https://www.acmicpc.net/problem/tag/71)

## 메모

올바른 괄호인지 확인 하는 함수를 사용하면 쉽게 풀림.

[올바른 괄호인지 판별](https://www.notion.so/fb2a9c35ed174c2d91c45ea825b7a0cc?pvs=21)
'''