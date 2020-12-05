import string 

lower = string.ascii_lowercase 
upper = string.ascii_uppercase

def solution(s, n):
    answer = ''
    for i in s:
        if i in list(lower):
            answer += str(list(lower)[(list(lower).index(i)+n)%26])
        elif i in list(upper):
            answer += str(list(upper)[(list(upper).index(i)+n)%26])
        else:
            answer += i
    return answer
