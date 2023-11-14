import sys


n = int(sys.stdin.readline())
datas = [sys.stdin.readline().strip() for _ in range(n)]

for data in datas:
    data = list(map(int, data.split()))
    x1, y1, r1, x2, y2, r2 = data
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if (x1, y1, r1) == (x2, y2, r2):
        print(-1)
    elif (r1 + r2 < d) or (abs(r1 - r2) > d) or (d == 0 and r1 != r2):
        print(0)
    elif (r1 + r2 == d) or abs(r1 - r2) == d:
        print(1)
    elif abs(r1 - r2) < d < (r1 + r2):
        print(2)


# # 터렛

# | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
# | --- | --- | --- | --- | --- | --- |
# | 2 초 | 128 MB | 204238 | 45490 | 34915 | 22.414% |

# ## 문제

# 조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.

# !https://www.acmicpc.net/upload/201003/dfcmhrjj_142c3w76qg8_b.jpg

# 이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

# 조규현의 좌표 (�1,�1)$(x_1, y_1)$와 백승환의 좌표 (�2,�2)$(x_2, y_2)$가 주어지고, 조규현이 계산한 류재명과의 거리 �1$r_1$과 백승환이 계산한 류재명과의 거리 �2$r_2$가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

# ## 입력

# 첫째 줄에 테스트 케이스의 개수 �$T$가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

# 한 줄에 공백으로 구분 된 여섯 정수 �1$x_1$, �1$y_1$, �1$r_1$, �2$x_2$, �2$y_2$, �2$r_2$가 주어진다.

# ## 출력

# 각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 −1$-1$ 출력한다.

# ## 제한

# - $-10\,000 ≤ x_1, y_1, x_2, y_2 ≤ 10\,000$
    
#     −10000≤�1,�1,�2,�2≤10000
    
# - $1 ≤ r_1, r_2 ≤ 10\,000$
    
#     1≤�1,�2≤10000
    

# ## 예제 입력 1

# ```
# 3
# 0 0 13 40 0 37
# 0 0 3 0 7 4
# 1 1 1 1 1 5

# ```

# ## 예제 출력 1

# ```
# 2
# 1
# 0

# ```

# ## 출처

# - 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
# - 문제의 오타를 찾은 사람: [baemin0103](https://www.acmicpc.net/user/baemin0103), [koyh1200](https://www.acmicpc.net/user/koyh1200)
# - 데이터를 추가한 사람: [dksdks3737](https://www.acmicpc.net/user/dksdks3737), [doju](https://www.acmicpc.net/user/doju)

# ## 알고리즘 분류

# [보기](https://www.acmicpc.net/problem/1002#)

# ## 메모

# 두 점: 두 원의 직선 거리 < 원의 반지름의 합.

# 한 점: 두 원의 직선 거리 = 원의 반지름의 합.

# 0: 두 원의 직선 거리 > 원의 반지름의 합.

# -1: 같은 중심점, 같은 반지름.

# [두 원의 위치에 따른 접점 개수.](https://www.notion.so/05359a2bfc2d419b94aea0de8d0c87d5?pvs=21)

# [Python input() → sys.stdin.readline()](https://www.notion.so/Python-input-sys-stdin-readline-605d71aa01db420bb2e3cdf01d577513?pvs=21)
