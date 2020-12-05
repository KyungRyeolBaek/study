def solution(numbers):
    answer = [a + b for a in sorted(numbers) for b in sorted(numbers)]
    for a in [2*a for a in sorted(numbers)]:
        answer.remove(a)
    return list(set(answer))
