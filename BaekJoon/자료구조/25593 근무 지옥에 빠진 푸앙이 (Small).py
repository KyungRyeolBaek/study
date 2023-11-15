import sys
input = sys.stdin.readline

N = int(input())
time = [4, 6, 4, 10]
schedule = {}
for _ in range(N):
    for t in time:
        names = input().split()
        for name in names:
            if name != '-':
                if name not in schedule:
                    schedule[name] = t
                else:
                    schedule[name] += t

working_times = schedule.values()
if not schedule or max(working_times) - min(working_times) <= 12:
    print('Yes')
else:
    print('No')

# # 근무 지옥에 빠진 푸앙이 (Small)

# | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
# | --- | --- | --- | --- | --- | --- |
# | 1 초 | 1024 MB | 424 | 212 | 191 | 51.206% |

# ## 문제

# 군대에 간 푸앙이는 4교대 근무를 서게 된다. 근무 시간대는 08:00~12:00, 12:00~18:00, 18:00~22:00, 22:00~08:00 으로 각각 4, 6, 4, 10시간의 근무로 구성되어 있다.

# 푸앙이와 동기들은 근무 시간이 최대한 공평하게 배분되기를 원한다. 그래서 근무표 전체에서 각 인원의 근무 시간이 12시간 이하로 차이 나게 해서 최대 50주 치 근무표를 짜려고 한다.

# 푸앙이는 원래 똑똑해서 이 정도는 한눈에 계산이 가능했지만 어째서인지 푸앙이는 계산이 불가능해졌다. 푸앙이를 위해서 대신 근무표가 공평한지 계산해주자.

# ## 입력

# 첫 번째 줄에 주의 개수인 �$N$이 입력된다. (1≤�≤50)$(1 \leq N \leq 50)$

# 둘째 줄부터 근무표가 주어진다. 각 주는 4개의 줄로 표현되며, 그중 첫째 줄은 각 날의 08:00~12:00에 근무하는 사람의 이름 또는 '-', 둘째 줄은 12:00~18:00, 셋째 줄은 18:00~22:00, 넷째 줄은 22:00~08:00을 나타낸다. '-'는 근무자가 없음을 의미한다. 근무자의 이름은 모두 알파벳 소문자로 이루어져 있고 20글자를 넘지 않는다.

# 각 날에는 4개의 시간대에 모두 근무자가 있거나 모두 근무자가 없다. 예를 들어 12:00~18:00에만 근무자가 있는 날은 없다.

# 근무표에 적히지 않은 근무자는 없으며, 근무자 수는 최대 100$100$명이다.

# ## 출력

# 근무표가 공평하면 “`Yes`”를 아니면 “`No`”를 출력한다. 단, 아무도 근무하지 않을 경우 공평한 것으로 간주한다.

# ## 예제 입력 1

# ```
# 4
# - - - - - pangyo puang
# - - - - - sally boss
# - - - - - leonard brown
# - - - - - edward edward
# puang pangyo choco leonard cony leonard choco
# cony edward cony leonard moon puang edward
# choco boss puang brown brown pangyo cony
# choco edward puang cony moon choco boss
# brown moon moon sally pangyo puang choco
# pangyo edward boss sally moon cony pangyo
# brown puang james moon cony choco choco
# sally brown sally puang james moon sally
# leonard pangyo - - - - -
# boss choco - - - - -
# moon edward - - - - -
# moon sally - - - - -

# ```

# ## 예제 출력 1

# ```
# No

# ```

# ## 예제 입력 2

# ```
# 4
# - - - - - sally boss
# - - - - - brown boss
# - - - - - moon sally
# - - - - - leonard edward
# pangyo moon cony boss james sally brown
# moon brown sally cony brown choco edward
# moon leonard pangyo moon edward puang puang
# leonard sally boss choco cony boss edward
# brown sally jessica leonard moon jessica james
# jessica brown leonard puang james pangyo puang
# puang choco james cony jessica pangyo jessica
# pangyo jessica choco james puang cony pangyo
# moon moon james choco edward - -
# jessica brown james sally puang - -
# cony leonard moon boss choco - -
# edward jessica cony brown leonard - -

# ```

# ## 예제 출력 2

# ```
# Yes

# ```

# ## 힌트

# 첫 번째 예제에서 둘째 주 첫날 08:00~12:00 근무자는 puang, 12:00~18:00 근무자는 cony, 18:00~22:00 근무자는 choco, 22:00~08:00 근무자는 choco이다.

# 두 번째 예제에서 둘째 주 첫날 08:00~12:00 근무자는 pangyo, 12:00~18:00 근무자는 moon, 18:00~22:00 근무자는 moon, 22:00~08:00 근무자는 leonard이다.

# ## 출처

# [University](https://www.acmicpc.net/category/5) > [중앙대학교](https://www.acmicpc.net/category/400) > [2022 중앙대학교 프로그래밍 경진대회(CPC)](https://www.acmicpc.net/category/803) > [Division 2](https://www.acmicpc.net/category/detail/3188) C번

# - 문제를 검수한 사람: [hibye1217](https://www.acmicpc.net/user/hibye1217), [jh05013](https://www.acmicpc.net/user/jh05013), [jthis](https://www.acmicpc.net/user/jthis), [kclee2172](https://www.acmicpc.net/user/kclee2172), [njw1204](https://www.acmicpc.net/user/njw1204), [tony9402](https://www.acmicpc.net/user/tony9402)
# - 문제를 만든 사람: [smmaker118](https://www.acmicpc.net/user/smmaker118)

# ## 알고리즘 분류

# - [구현](https://www.acmicpc.net/problem/tag/102)
# - [자료 구조](https://www.acmicpc.net/problem/tag/175)
# - [문자열](https://www.acmicpc.net/problem/tag/158)
# - [해시를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/136)

# ## 메모

# 출력문 .. 앞글자만 대문자. 뒤는 소문자.

# 예외 처리. 아무도 일 안하는날은 Yes.
