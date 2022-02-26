import numpy as np

def solution(numbers, target):
    target_list = []
    
    for x in range(2**len(numbers)):
        target_list.append(np.array([1 if s != '0' else -1 for s in bin(x)[2:].rjust(len(numbers), '0')]))
    
    answer = 0
    for t in target_list:
        if sum(np.array(numbers) * t) == target:
            answer += 1
        
    return answer

### 메모
# 이진수, np.array 연산

# 다른 풀이
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# 메모
# 재귀함수, 빠름

# 다른 풀이
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

# 메모
# itertools의 product 함수, 가장 빠름
# https://www.notion.so/Python-product-itertools-1311c62b2ea94dd6b395471f37033fc8

# 다른풀이
def dfs(nums, i, n, t):
    ret = 0
    if i==len(nums):
        if n==t: return 1
        else: return 0
    ret += dfs(nums, i+1, n+nums[i], t)
    ret += dfs(nums, i+1, n-nums[i], t)
    return ret

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer

# 메모
# DFS, 재귀함수 : https://www.notion.so/N533-BFS-DFS-0a882d12f04f4ec59d6cfe17cd65cbca
# 정석 풀이

# 타겟 넘버
# 문제 설명
# n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
# 입출력 예
# numbers	target	return
# [1, 1, 1, 1, 1]	3	5
# [4, 1, 2, 1]	4	2
# 입출력 예 설명
# 입출력 예 #1

# 문제 예시와 같습니다.

# 입출력 예 #2

# +4+1-2+1 = 4
# +4-1+2-1 = 4
# 총 2가지 방법이 있으므로, 2를 return 합니다.