def solution(d, budget):
    for i, j in enumerate(sorted(d)):
        if budget-j < 0:
            return i
        elif budget-j == 0:
            return i + 1
        else:
            budget = budget-j
