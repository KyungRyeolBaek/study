def solution(n, m):
    a = n*m
    while m:
        n, m = m, n%m
    return [n, a/n]
