import math
import itertools

# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False # 2 이하 소수 아님
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(nums):
    # 주어진 nums에 따른 3가지 다른 숫자 합 경우의 수
    add_nums = [sum(num) for num in list(itertools.combinations((nums),3))]
    
    # 소수 판별
    answer = 0
    
    for num in add_nums:
        if is_prime_number(num):
            answer += 1
            
    return answer

# 조합 : [https://www.notion.so/Python-6b6faa99bab14c9cbc1f850e07182506?showMoveTo=true](https://www.notion.so/Python-6b6faa99bab14c9cbc1f850e07182506)
# 소수 판별 : [https://www.notion.so/7ef40f8788104ac98a41cd5296c8929e](https://www.notion.so/7ef40f8788104ac98a41cd5296c8929e)


# from itertools import combinations

# def prime_number(x):
#     answer = 0
#     for i in range(1,int(x**0.5)+1):
#         if x%i==0:
#             answer+=1
#     return 1 if answer==1 else 0

# def solution(nums):
#     return sum([prime_number(sum(c)) for c in combinations(nums,3)])



# 소수 만들기
# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
# 입출력 예
# nums	result
# [1,2,3,4]	1
# [1,2,7,6,4]	4
# 입출력 예 설명
# 입출력 예 #1
# [1,2,4]를 이용해서 7을 만들 수 있습니다.

# 입출력 예 #2
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
# [1,4,6]을 이용해서 11을 만들 수 있습니다.
# [2,4,7]을 이용해서 13을 만들 수 있습니다.
# [4,6,7]을 이용해서 17을 만들 수 있습니다.