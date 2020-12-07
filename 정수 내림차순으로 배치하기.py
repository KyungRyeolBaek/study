def solution(n):
    return int(''.join(reversed(sorted([i for i in str(n)]))))
