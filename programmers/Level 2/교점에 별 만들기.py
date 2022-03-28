from itertools import combinations
import numpy as np

def cross_point(line):
    A, B, E = line[0]
    C, D, F = line[1]
    if A*D-B*C != 0:
        x = (B*F-E*D)/(A*D-B*C)
        y = (E*C-A*F)/(A*D-B*C)
        if int(x) == x and int(y) == y:
            return int(x), int(y)
    else:
        return None

def solution(line):
    l = list(combinations(line, 2))
    less_x, less_y, max_x, max_y = np.inf, np.inf, -np.inf, -np.inf
    points = []
    for line in l:
        if cross_point(line):
            x, y = cross_point(line)
            points.append([x, y])
            if x < less_x:  less_x = x
            if y < less_y:  less_y = y
            if x > max_x:   max_x = x 
            if y > max_y:   max_y = y
            
    points = np.array(points)
    points = points - [less_x, less_y]
    max_x, max_y = max_x - less_x + 1, max_y - less_y + 1
    answer = [['.' for _ in range(max_x)] for _ in range(max_y)]
    for x, y in points:
        answer[y][x] = '*'
    
    return [''.join(i) for i in reversed(answer)]

### 메모
# 주어진 식을 사용하고, x와 y의 최소, 최대값을 찾아 시작점을 0, 0 으로 맞추고 끝점도 구해서 구해진 포인트에 별을 넣어주고 리스트 역순 취하면 된다.
# itertools combinations : [https://www.notion.so/Python-product-itertools-1311c62b2ea94dd6b395471f37033fc8](https://www.notion.so/Python-product-itertools-1311c62b2ea94dd6b395471f37033fc8)
# numpy array로 배열 내 계산




# 교점에 별 만들기
# 문제 설명
# Ax + By + C = 0으로 표현할 수 있는 n개의 직선이 주어질 때, 이 직선의 교점 중 정수 좌표에 별을 그리려 합니다.

# 예를 들어, 다음과 같은 직선 5개를

# 2x - y + 4 = 0
# -2x - y + 4 = 0
# -y + 1 = 0
# 5x - 8y - 12 = 0
# 5x + 8y + 12 = 0
# 좌표 평면 위에 그리면 아래 그림과 같습니다.

# RisingStarGraphBox.jpg

# 이때, 모든 교점의 좌표는 (4, 1), (4, -4), (-4, -4), (-4, 1), (0, 4), (1.5, 1.0), (2.1, -0.19), (0, -1.5), (-2.1, -0.19), (-1.5, 1.0)입니다. 이 중 정수로만 표현되는 좌표는 (4, 1), (4, -4), (-4, -4), (-4, 1), (0, 4)입니다.

# 만약 정수로 표현되는 교점에 별을 그리면 다음과 같습니다.

# RisingStarGraphStar.jpg

# 위의 그림을 문자열로 나타낼 때, 별이 그려진 부분은 *, 빈 공간(격자선이 교차하는 지점)은 .으로 표현하면 다음과 같습니다.

# "..........."  
# ".....*....."  
# "..........."  
# "..........."  
# ".*.......*."  
# "..........."  
# "..........."  
# "..........."  
# "..........."  
# ".*.......*."  
# "..........."  
# 이때 격자판은 무한히 넓으니 모든 별을 포함하는 최소한의 크기만 나타내면 됩니다.

# 따라서 정답은

# "....*...."  
# "........."  
# "........."  
# "*.......*"  
# "........."  
# "........."  
# "........."  
# "........."  
# "*.......*"  
# 입니다.

# 직선 A, B, C에 대한 정보가 담긴 배열 line이 매개변수로 주어집니다. 이때 모든 별을 포함하는 최소 사각형을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# line의 세로(행) 길이는 2 이상 1,000 이하인 자연수입니다.
# line의 가로(열) 길이는 3입니다.
# line의 각 원소는 [A, B, C] 형태입니다.
# A, B, C는 -100,000 이상 100,000 이하인 정수입니다.
# 무수히 많은 교점이 생기는 직선 쌍은 주어지지 않습니다.
# A = 0이면서 B = 0인 경우는 주어지지 않습니다.
# 정답은 1,000 * 1,000 크기 이내에서 표현됩니다.
# 별이 한 개 이상 그려지는 입력만 주어집니다.
# 입출력 예
# line	result
# [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]	["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]
# [[0, 1, -1], [1, 0, -1], [1, 0, 1]]	["*.*"]
# [[1, -1, 0], [2, -1, 0]]	["*"]
# [[1, -1, 0], [2, -1, 0], [4, -1, 0]]	["*"]
# 입출력 예 설명
# 입출력 예 #1

# 문제 예시와 같습니다.

# 입출력 예 #2

# 직선 y = 1, x = 1, x = -1는 다음과 같습니다.
# RisingStarGraphTC2.png

# (-1, 1), (1, 1) 에서 교점이 발생합니다.

# 따라서 정답은

# "*.*"  
# 입니다.

# 입출력 예 #3

# 직선 y = x, y = 2x는 다음과 같습니다.

# RisingStarGraphTC3.png

# (0, 0) 에서 교점이 발생합니다.

# 따라서 정답은

# "*"  
# 입니다.

# 입출력 예 #4

# 직선 y = x, y = 2x, y = 4x는 다음과 같습니다.

# RisingStarGraphTC4.png

# (0, 0) 에서 교점이 발생합니다.

# 따라서 정답은

# "*"
# 입니다.

# 참고 사항
# Ax + By + E = 0
# Cx + Dy + F = 0
# 두 직선의 교점이 유일하게 존재할 경우, 그 교점은 다음과 같습니다.

# RisingStarExpression.png

# 또, AD - BC = 0인 경우 두 직선은 평행 또는 일치합니다.