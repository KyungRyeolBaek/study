import sys


N = int(input())
have_cards = set(input().strip().split())
M = int(input())
searching_cards = input().strip().split()

result = []
for card in searching_cards:
    if card in have_cards:
        result.append(str(1))
    else:
        result.append(str(0))
print(' '.join(result))