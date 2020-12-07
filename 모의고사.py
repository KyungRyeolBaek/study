def solution(answers):
    r = [len([+1 for i in range(len(answers)) if answers[i] == [1, 2, 3, 4, 5][i%5]]),
        len([+1 for i in range(len(answers)) if answers[i] == [2, 1, 2, 3, 2, 4, 2, 5][i%8]]),
        len([+1 for i in range(len(answers)) if answers[i] == [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][i%10]])]
    if r == [0,0,0]:
        return []
    return [i+1 for i in range (3) if max(r) == r[i]]
    
# max(list) list의 최대값 찾아줌.
