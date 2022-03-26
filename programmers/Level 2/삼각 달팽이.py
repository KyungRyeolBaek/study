def solution(n):
    answer = [[0]*(i+1) for i in range(n)]
    num = 1
    down_idx = 0
    right_idx = 0
    up_idx = 0
    for i in range(n):
        if i % 3 == 0:
            for j in range(n-i):
                answer[j+down_idx+up_idx][down_idx] = num
                num += 1
            down_idx += 1
        elif i % 3 == 1:
            for j in range(n-i):
                answer[n-right_idx-1][down_idx+j] = num
                num += 1
            right_idx += 1
        else:
            for j in range(n-i):
                answer[n-right_idx-1-j][-up_idx-1] = num
                num += 1
            up_idx += 1
    return [n for l in answer for n in l]

### 메모
# list comprehension : [https://www.notion.so/Python-2-1-itertools-ec2f1c9244e14c6d9a4bcbbbbeacf24f](https://www.notion.so/Python-2-1-itertools-ec2f1c9244e14c6d9a4bcbbbbeacf24f)



# 삼각 달팽이
# 문제 설명
# 정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

# examples.png

# 제한사항
# n은 1 이상 1,000 이하입니다.
# 입출력 예
# n	result
# 4	[1,2,9,3,10,8,4,5,6,7]
# 5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
# 6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
# 입출력 예 설명
# 입출력 예 #1

# 문제 예시와 같습니다.
# 입출력 예 #2

# 문제 예시와 같습니다.
# 입출력 예 #3

# 문제 예시와 같습니다.