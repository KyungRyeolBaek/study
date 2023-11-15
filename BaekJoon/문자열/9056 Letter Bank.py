import sys

N = int(sys.stdin.readline())

for _ in range(N):
    A, B = map(set, sys.stdin.readline().split())
    if A - B or B - A:
        print('NO')
    else:
        print('YES')

# # Letter Bank 다국어

# | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
# | --- | --- | --- | --- | --- | --- |
# | 1 초 | 128 MB | 203 | 153 | 139 | 77.654% |

# ## 문제

# A letter bank is a word such that all the letters of one letter bank can be used as many times as desired (at least once each) to make a new word. For example, ‘IMPS’ is a bank of ‘MISSISSIPPI.’

# Given two words α and β, you are to write a program for deciding whether α is a bank of β. Assume that the first word α has no repeated letters. Every word consists only of capital Roman letters: A, B, …, Z, and no blank.

# ## 입력

# Your program is to read from standard input. The input consists of T (1 ≤ T ≤ 20) test cases. The number T of test case is given in the first line of the input. For each test case, two words are given in one line. There is a single space between the first word and the second word. And each word has length at most 80.

# ## 출력

# Your program is to write a standard output. Print exactly one line for each test case. For each test case, print “YES” if the first word is a bank of the second word. Otherwise, print “NO”.

# ## 예제 입력 1

# ```
# 4
# IMPS MISSISSIPPI
# BLUE BLUE
# CNT COCONUT
# IPC PC

# ```

# ## 예제 출력 1

# ```
# YES
# YES
# NO
# NO

# ```

# ## 출처

# [ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [Asia Pacific](https://www.acmicpc.net/category/42) > [Korea](https://www.acmicpc.net/category/211) > [Nationwide Internet Competition](https://www.acmicpc.net/category/256) > [Seoul Nationalwide Internet Competition 2007](https://www.acmicpc.net/category/detail/1086) A번

# - 데이터를 추가한 사람: [measurezero](https://www.acmicpc.net/user/measurezero)

# ## 알고리즘 분류

# - [구현](https://www.acmicpc.net/problem/tag/102)
# - [자료 구조](https://www.acmicpc.net/problem/tag/175)
# - [문자열](https://www.acmicpc.net/problem/tag/158)
# - [해시를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/136)

# ## 메모
