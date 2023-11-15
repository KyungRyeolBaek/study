import sys

input = sys.stdin.readline

L, G, R = map(int, input().split())

lamps = [0 for _ in range(L + 1)]

gards = {}
for _ in range(G):
    gard, a0, d = input().split()
    route = []
    last = int(a0)
    while last <= L:
        route.append(last)
        last += int(d)
    gards[gard] = route

for _ in range(R):
    for lamp in gards[input().split()[0]]:
        if lamps[lamp]:
            lamps[lamp] = 0
        else:
            lamps[lamp] = 1

print(sum(lamps))

# # Lamp 다국어

# | 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
# | --- | --- | --- | --- | --- | --- |
# | 1 초 | 128 MB | 85 | 54 | 50 | 65.789% |

# ## 문제

# A building has a long corridor and *L* ceiling lamps labeled 1, 2, 3, ..., *L*. Each lamp has an individual switch that can turn the lamp on or off. The building manager hires *G* security guards (no two guards have the same name), whose job at night is to patrol the corridor and turn the lamps on and off. Each guard is assigned a subset of lamps. During one patrol round, a guard will walk along the corridor, and toggle the lamps assigned to him/her (that is, if a lamp is on, switch it off; if the lamp is off, switch it on). After a guard toggles each lamp assigned to him/her exactly once, the guard will take a break until his/her next patrol round. A guard may have more than one patrol round in one night. The order of patrol for the guards is dictated by a duty roster.

# All lamps are off before the guards begin their patrol rounds, and there is only one guard on patrol at any time.

# The assignment of lamps to a guard is specified by two positive integers, *a*0 and *d*. The subset of lamps the guard will toggle is

# {*a*0, *a*0 + *d*, *a*0 + 2*d*, ..., *a*0 + *kd*}

# where *k* is the largest integer such that *a*0 + *kd* ≤ *L*.

# Given the lamp assignment for each guard and the duty roster, find out how many lamps are on after all the guards have finished all of their patrol rounds.

# Suppose we have 10 lamps, two security guards (Edi and Lou), and three patrol rounds. Edi's lamp assignment is (*a*0, *d*) = (1, 4) and Lou's lamp assignment is (*a*0, *d*) = (2, 3). The order of patrol is Edi, Lou, Edi.

# After the first patrol round by Edi, lamps 1, 5, and 9 will be on. During the second patrol round, Lou toggles lamps 2, 5, and 8. Therefore, after the second patrol round, lamps 1, 2, 8, and 9 are on but lamp 5 has been turned off. On the third patrol round, Edi patrols again, and toggles lamps 1, 5, and 9. Consequently, after all the patrol rounds specified in the duty roster, the lamps that are on are 2, 5, and 8.

# The number of lamps that are still on after the guards finish their patrol rounds is therefore 3.

# ## 입력

# The first line in input consists of three positive integers, separated with a blank character. The first number *L* ≤ 1000 is the number of lamps. The second number *G* ≤ 10 is the number of security guards, and the third number *R* ≤ 50 is the total number of patrol rounds. The next *G* lines contain the names and lamp assignments of the guards. Each of these *G* lines consists of the name (exactly 3 English letters), *a*0 and *d*, (*a*0 ≤ *N*) separated with a blank character. The subsequent *R* lines specify the duty roster. Each line contains the name of a guard (guaranteed to have lamp assignment). The order of the guards appearing in the duty roster dictates the order of their patrol.

# ## 출력

# The output contains one integer which is the number of lamps that are on after all guards finish all of their patrol rounds.

# ## 예제 입력 1

# ```
# 10 2 3
# Edi 1 4
# Lou 2 3
# Edi
# Lou
# Edi

# ```

# ## 예제 출력 1

# ```
# 3

# ```

# ## 출처

# [Olympiad](https://www.acmicpc.net/category/2) > [National Olympiad in Informatics (Singapore)](https://www.acmicpc.net/category/292) > [NOI 2004](https://www.acmicpc.net/category/detail/1223) 2번

# ## 알고리즘 분류

# - [구현](https://www.acmicpc.net/problem/tag/102)
# - [자료 구조](https://www.acmicpc.net/problem/tag/175)
# - [문자열](https://www.acmicpc.net/problem/tag/158)
# - [브루트포스 알고리즘](https://www.acmicpc.net/problem/tag/125)
# - [시뮬레이션](https://www.acmicpc.net/problem/tag/141)
# - [해시를 사용한 집합과 맵](https://www.acmicpc.net/problem/tag/136)

# ## 메모

# 하나 하나 차근차근 풀면 풀린다.

# 부호 조심 ≤ L

# 마지막 순찰 이름 때 개행 문자 포함됨.
