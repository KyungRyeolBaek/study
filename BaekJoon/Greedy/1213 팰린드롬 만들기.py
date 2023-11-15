import sys
input = sys.stdin.readline

S = input().rstrip()

string_dict = {}
for s in S:
    if s in string_dict:
        string_dict[s] += 1
    else:
        string_dict[s] = 1

odd, even = [], []
result, left = '', ''
for key, value in string_dict.items():
    if value % 2 == 0:
        even.append(key)
    else:
        odd.append(key)

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    if odd:
        tmp = odd.pop()
        result = tmp
        string_dict[tmp] -= 1
        if string_dict[tmp] != 0:
            even.append(tmp)
    even.sort(reverse=True)
    while even:
        tmp = even.pop()
        left += tmp * int(string_dict[tmp] / 2)
    result = left + result + left[::-1]

    print(result)


# # 팰린드롬 만들기

# | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
# | --- | --- | --- | --- | --- | --- |
# | 2 초 | 128 MB | 21272 | 8866 | 6943 | 41.056% |

# ## 문제

# 임한수와 임문빈은 서로 사랑하는 사이이다.

# 임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.

# 임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.

# 임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

# ## 입력

# 첫째 줄에 임한수의 영어 이름이 있다. 알파벳 대문자로만 된 최대 50글자이다.

# ## 출력

# 첫째 줄에 문제의 정답을 출력한다. 만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다. 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.

# ## 예제 입력 1

# ```
# AABB

# ```

# ## 예제 출력 1

# ```
# ABBA
# ```

# ## 예제 입력 2

# ```
# AAABB

# ```

# ## 예제 출력 2

# ```
# ABABA

# ```

# ## 예제 입력 3

# ```
# ABACABA

# ```

# ## 예제 출력 3

# ```
# AABCBAA

# ```

# ## 예제 입력 4

# ```
# ABCD

# ```

# ## 예제 출력 4

# ```
# I'm Sorry Hansoo

# ```

# ## 출처

# - 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

# ## 알고리즘 분류

# - [구현](https://www.acmicpc.net/problem/tag/102)
# - [문자열](https://www.acmicpc.net/problem/tag/158)
# - [그리디 알고리즘](https://www.acmicpc.net/problem/tag/33)

# ## 메모

# 각 글자별로 개수와 함께 dictionary에 넣어 놓는다.

# 홀수인 값을 먼저 결과에 넣어 놓고. 홀수의 개수를 1개 뺀다. 그리고 짝수의 글자에 넣는다.

# 짝수인 값들을 정렬한다.

# 왼쪽 결과값에 짝수인 값 하나를 꺼내와 dictionary에 적힌 개수의 절반만큼 추가한다.

# 위를 짝수인 값이 없어질 때 까지 반복한다.

# 결과값에 왼쪽값과, 왼쪽값을 대치 시킨 오른쪽 값을 붙인다. 

# 끝
