def solution(num):
    answer = 0
    for i in range(500):
        if i == 499:
            return -1
        if num == 1:
            return answer
        elif num % 2 == 0:
            num = num / 2
            answer += 1
        else:
            num = (num*3)+1
            answer += 1
    return answer
