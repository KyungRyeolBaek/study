import sys

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid(grid, num, pos):
    row, col = pos
    
    # Check the row
    for j in range(9):
        if grid[row][j] == num:
            return False

    # Check the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check the box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    find = find_empty(grid)
    if not find:
        return True  # 모든 빈칸을 채운 경우

    row, col = find

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

def main():
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    
    solve_sudoku(grid)
    
    for row in grid:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()


'''
# 스도쿠 스페셜 저지

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 104420 | 30713 | 19537 | 27.055% |

## 문제

스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다. 이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데, 게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.

https://upload.acmicpc.net/508363ac-0289-4a92-a639-427b10d66633/-/preview/

나머지 빈 칸을 채우는 방식은 다음과 같다.

1. 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
2. 굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.

위의 예의 경우, 첫째 줄에는 1을 제외한 나머지 2부터 9까지의 숫자들이 이미 나타나 있으므로 첫째 줄 빈칸에는 1이 들어가야 한다.

https://upload.acmicpc.net/38e505c6-0452-4a56-b01c-760c85c6909b/-/preview/

또한 위쪽 가운데 위치한 3x3 정사각형의 경우에는 3을 제외한 나머지 숫자들이 이미 쓰여있으므로 가운데 빈 칸에는 3이 들어가야 한다.

https://upload.acmicpc.net/89873d9d-56ae-44f7-adb2-bd5d7e243016/-/preview/

이와 같이 빈 칸을 차례로 채워 가면 다음과 같은 최종 결과를 얻을 수 있다.

https://upload.acmicpc.net/fe68d938-770d-46ea-af71-a81076bc3963/-/preview/

게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

## 입력

아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다. 스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

## 출력

모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.

스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.

## 제한

- 12095번 문제에 있는 소스로 풀 수 있는 입력만 주어진다.
    - C++14: 80ms
    - Java: 292ms
    - PyPy3: 1172ms

## 예제 입력 1

```
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0

```

## 예제 출력 1

```
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1

```

## 출처

[Olympiad](https://www.acmicpc.net/category/2) > [한국정보올림피아드](https://www.acmicpc.net/category/55) > [한국정보올림피아드시․도지역본선](https://www.acmicpc.net/category/57) > [지역본선 2006](https://www.acmicpc.net/category/70) > [초등부](https://www.acmicpc.net/category/detail/367) 5번

[Olympiad](https://www.acmicpc.net/category/2) > [한국정보올림피아드](https://www.acmicpc.net/category/55) > [한국정보올림피아드시․도지역본선](https://www.acmicpc.net/category/57) > [지역본선 2006](https://www.acmicpc.net/category/70) > [중등부](https://www.acmicpc.net/category/detail/368) 3번

- 데이터를 추가한 사람: [doju](https://www.acmicpc.net/user/doju)

## 알고리즘 분류

- [백트래킹](https://www.acmicpc.net/problem/tag/5)

## 메모

일반적인 방법 백트래킹으로 풀이. → 시간 초과 

MRV를 이용한 백트래킹 → 시간 초과 [백트래킹](https://www.notion.so/8d53884eba3f476db757f053a91bf0de?pvs=21) 

안되서 pypy3로 품.. 나중에 아래 과정으로 풀이 진행.

아래는 심화 과정으로 풀이.

[Algorithm X와 DLX의 결합: 스도쿠 문제 해결](https://www.notion.so/Algorithm-X-DLX-71ae79bfb3c64b5f8f8ca872a2ced385?pvs=21)
'''