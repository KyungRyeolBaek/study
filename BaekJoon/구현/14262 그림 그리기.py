import sys
input = sys.stdin.readline

# 시작점 좌표가 1, 1씩 늘어남.
# 초기 행, 열에 각각 T초 만큼 추가.
row, col, T = map(int, input().rstrip().split())
canvas = [[0 for _ in range(col + T)] for _ in range(row + T)]
board = [list(input().rstrip()) for _ in range(row)]
color = {'R': 0, 'G': 0, 'B': 0}
for t in range(T):
    for r in range(row):
        for c in range(col):
            if board[r][c] != '.':
                if canvas[r + t][c + t]:
                    color[canvas[r + t][c + t]] -= 1
                color[board[r][c]] += 1
                canvas[r + t][c + t] = board[r][c]

for res in color.values():
    print(res)
