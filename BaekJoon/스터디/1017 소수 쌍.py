import sys
import math


# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False        # 2 이하 소수 아님
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False    # 소수가 아님
    return True             # 소수임


def find_all_pairs(lst):
    def backtrack(start, path):
        if len(path) == len(lst) // 2:
            result.append(path)
            return
        for i in range(start, len(lst)):
            for j in range(i + 1, len(lst)):
                if not used[i] and not used[j]:
                    used[i] = True
                    used[j] = True
                    backtrack(i + 1, path + [(lst[i], lst[j])])
                    used[i] = False
                    used[j] = False
            print(result)

    result = []
    used = [False] * len(lst)
    backtrack(0, [])
    return result


input = sys.stdin.readline
N = int(input().strip())
_list = list(map(int, input().strip().split()))
answer = set([])
for pair in find_all_pairs(_list):
    for p in pair:
        if not is_prime_number(sum(p)):
            break
    else:
        answer.add(pair[0][1])
    print(pair)
if answer:
    print(' '.join(map(str, sorted(answer))))
else:
    print(-1)
