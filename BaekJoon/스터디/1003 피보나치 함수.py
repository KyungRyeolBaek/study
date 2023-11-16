import sys


def fibonacci(n):
    return int(((1 + 5**0.5)**n - (1 - 5**0.5)**n) / ((2**n) * (5**0.5)))


n = int(sys.stdin.readline())
datas = [int(sys.stdin.readline().strip()) for _ in range(n)]

for data in datas:
    result = [fibonacci(abs(data - 1)), fibonacci(data)]
    print('{} {}'.format(*result))


'''
다이나믹 프로그래밍.
'''
# # 피보나치 함수

# | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
# | --- | --- | --- | --- | --- | --- |
# | 0.25 초 (추가 시간 없음) | 128 MB | 204464 | 62079 | 48923 | 32.798% |

# ## 문제

# 다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

# ```
# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }

# ```

# `fibonacci(3)`을 호출하면 다음과 같은 일이 일어난다.

# - `fibonacci(3)`은 `fibonacci(2)`와 `fibonacci(1)` (첫 번째 호출)을 호출한다.
# - `fibonacci(2)`는 `fibonacci(1)` (두 번째 호출)과 `fibonacci(0)`을 호출한다.
# - 두 번째 호출한 `fibonacci(1)`은 1을 출력하고 1을 리턴한다.
# - `fibonacci(0)`은 0을 출력하고, 0을 리턴한다.
# - `fibonacci(2)`는 `fibonacci(1)`과 `fibonacci(0)`의 결과를 얻고, 1을 리턴한다.
# - 첫 번째 호출한 `fibonacci(1)`은 1을 출력하고, 1을 리턴한다.
# - `fibonacci(3)`은 `fibonacci(2)`와 `fibonacci(1)`의 결과를 얻고, 2를 리턴한다.

# 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, `fibonacci(N)`을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

# ## 입력

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

# ## 출력

# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

# ## 예제 입력 1

# ```
# 3
# 0
# 1
# 3

# ```

# ## 예제 출력 1

# ```
# 1 0
# 0 1
# 1 2

# ```

# ## 예제 입력 2

# ```
# 2
# 6
# 22

# ```

# ## 예제 출력 2

# ```
# 5 8
# 10946 17711

# ```

# ## 출처

# - 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
# - 데이터를 추가한 사람: [connotation](https://www.acmicpc.net/user/connotation), [doju](https://www.acmicpc.net/user/doju), [wonrok97](https://www.acmicpc.net/user/wonrok97)
# - 어색한 표현을 찾은 사람: [cyj101366](https://www.acmicpc.net/user/cyj101366)

# ## 알고리즘 분류

# [보기](https://www.acmicpc.net/problem/1003#)

# ## 메모

# 다이나믹 프로그래밍.
# 일반적으로 풀면 시간 초과가 뜸.
# 항등식 찾아서 함수로 구현하면 됨.
# [https://ko.wikipedia.org/wiki/피보나치_수](https://ko.wikipedia.org/wiki/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98_%EC%88%98)
