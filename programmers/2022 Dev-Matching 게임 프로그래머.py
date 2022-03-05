# 364 
# -------------
# 1. stack = [0 for _ in range(365)]
# 2. stack[구매 날짜 : 구매 날짜 + 30] += [구매 금액 for _ in range(30)]
# 3. 구매 날짜 + 30일이 12/31일을 넘길 경우 : += [구매 금액 for _ in range(365-구매날짜)]
# 4. 각 날짜별 등급 추출
# ----
# 오류 원인 검토
'''
x : purchase의 길이는 1 이상 365 이하입니다.
x : purchase의 원소는 "2019/MM/DD X" 형식입니다.
3에서 해결 : 2019/MM/DD는 2019년 MM월 DD일을 의미하며, "2019/01/01"에서 "2019/12/31"사이입니다.
정렬 의미 없음 : 구매 기록은 날짜 순으로 정렬되어 있습니다.
주어져도 상관 없음 : 같은 날짜의 구매 기록이 중복해서 주어지지 않습니다.
금액 상관 없음 : 'X'는 구매 금액을 나타내며 1,000 이상 200,000 이하인 자연수입니다.
x : 구매 금액은 1,000원 단위로만 주어집니다.
x : 정답 배열은 [브론즈 기간, 실버 기간, 골드 기간, 플래티넘 기간, 다이아몬드 기간] 순서로 채워서 return 해주세요.
'''


from datetime import datetime
from collections import Counter

def solution(purchase):
    # 1
    stack = [0 for _ in range(365)]
    for date in purchase:
        s_day = datetime.strptime('20190101', '%Y%m%d')
        b_day = datetime.strptime(date.split()[0].replace('/', ''), '%Y%m%d')
        
        p_day = (b_day - s_day).days
        p_max_day = 365 - p_day
        # 2
        if p_max_day >= 30:
            for i in range(30):
                stack[p_day+i] += int(date.split()[1])
        # 3
        elif p_max_day < 30:
            for j in range(p_max_day):
                stack[p_day+j] += int(date.split()[1])
    # 4
    for k in range(365):
        if stack[k] < 10000:
            stack[k] = 0
        elif stack[k] < 20000:
            stack[k] = 1
        elif stack[k] < 50000:
            stack[k] = 2
        elif stack[k] < 100000:
            stack[k] = 3
        else:
            stack[k] = 4
    
    # 오류 해결
    answer = [0 for _ in range(5)]
    # 0일경우 추가 되지 않음.
    for c, d in sorted(Counter(stack).items()):
        answer[c] = d

    return answer