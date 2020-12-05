def solution(numbers):
    return sorted(list(set([a + b for i, a in enumerate(numbers) for j, b in enumerate(numbers) if i != j])))
