from collections import deque

def solution(prices):
    answer = [i for i in range(len(prices)-1, 0, -1)] + [0]
    stack = deque()
    for idx, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            p = stack.pop()
            answer[p] = idx - p
        stack.append(idx)
            
    return answer


### 메모
# 끝까지 가격이 안내렸을 때를 베이스로 깔고, stack의 마지막 가격보다 낮은 가격이 나오면 해당 위치 answer 수정. - stack 사용
# collections deque : [https://www.notion.so/Deque-pop-push-64372aac99ea4b4a83b5feb6f61f70ec?showMoveTo=true](https://www.notion.so/Deque-pop-push-64372aac99ea4b4a83b5feb6f61f70ec)
# enumerate : [https://www.notion.so/Python-enumerate-6ae496d132c74d499f66595399224b6d](https://www.notion.so/Python-enumerate-6ae496d132c74d499f66595399224b6d)



# 주식가격
# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
# 입출력 예
# prices	return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
# 입출력 예 설명
# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
# ※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.