# import sys
# from itertools import permutations


# input = sys.stdin.readline

# operate = ['+', '-', '*', '/']
# N = int(input())
# nums = list(map(int, input().strip().split()))
# operate_count = list(map(int, input().strip().split()))
# opers = []
# for oper, count in zip(operate, operate_count):
#     for _ in range(count):
#         opers.append(oper)

# opers = list(permutations(opers, len(opers)))


def dfs(i, now, add, sub, mul, div):
    global min_value, max_value
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i], add, sub, mul, div)
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i], add, sub, mul, div)
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i], add, sub, mul, div)
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i], add, sub, mul, div))  # Python에서의 나눗셈 주의
            div += 1

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

dfs(1, data[0], add, sub, mul, div)

print(max_value)
print(min_value)
