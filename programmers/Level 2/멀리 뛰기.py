def solution(n):
    table = [0]*n
    table[0], table[1] = 1, 2
    
    for i in range(2, n):
        table[i] = table[i-1] + table[i-2]
        
    return table[-1] % 1234567

### 메모
# 첫번째, 두번째 위치까지 가는 방법의 개수의 합은 세번째 위치로 가는 개수
# table[n] = table[n-1] + table[n-2]


def function(n):
    global answer
    if n == 0:
        answer += 1
    else:
        if n >= 2:
            function(n-1)
            function(n-2)
        else:
            function(n-1)

            
def solution(n):
    global answer
    answer = 0
    function(n)
    return answer % 1234567

### 메모
# 재귀 함수 : [재귀함수 : **recursive function**](https://www.notion.so/recursive-function-0118a63220834c31be50d4ac49d07d98) 
# 전역 변수 : 사용될 함수에 전역 변수 호출


# 멀리 뛰기
# 문제 설명
# 효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
# (1칸, 1칸, 1칸, 1칸)
# (1칸, 2칸, 1칸)
# (1칸, 1칸, 2칸)
# (2칸, 1칸, 1칸)
# (2칸, 2칸)
# 의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.

# 제한 사항
# n은 1 이상, 2000 이하인 정수입니다.
# 입출력 예
# n	result
# 4	5
# 3	3
# 입출력 예 설명
# 입출력 예 #1
# 위에서 설명한 내용과 같습니다.

# 입출력 예 #2
# (2칸, 1칸)
# (1칸, 2칸)
# (1칸, 1칸, 1칸)
# 총 3가지 방법으로 멀리 뛸 수 있습니다.