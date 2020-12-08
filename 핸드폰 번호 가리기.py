def solution(phone_number):
    return ''.join(["*" for i in phone_number[:-4]]) + phone_number[-4:]
    
    
