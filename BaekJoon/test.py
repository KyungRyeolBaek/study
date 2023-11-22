# # sys.stdin.readline().rstrip()
# import sys

# L, G, R = map(int, sys.stdin.readline().rstrip().split())
# L_lst = [0 for __ in range(L)]
# G_lst = []
# R_lst = []
# for __ in range(G):
#     g = sys.stdin.readline().rstrip()
#     name, a, d = g.split()
#     a, d = int(a), int(d)
#     print(a, d)
#     num = a
#     cnt = 0
#     lst = []
#     while num <= L:
#         lst.append(num - 1)
#         cnt+=1
#         num = a + cnt * d
#     G_lst.append(lst)
#     R_lst.append(name)

# for __ in range(R):
#     name = sys.stdin.readline().rstrip()
#     lst = G_lst[R_lst.index(name)]
#     for i in lst:
#         if L_lst[i]:
#             L_lst[i] = 0
#         else:
#             L_lst[i] = 1

# print(L_lst.count(1))


import sys
import math


input = sys.stdin.readline

N = int(input())
F = int(input())

N = math.floor(N / 100) * 100
if (N % F) == 0:
    print('00')
else:
    result = str(((N // F) + 1) * F)[-2:]
    print(result)
