def min_special_forces(N, W, enemies):
    enemies.sort()  # 적의 수를 정렬
    total_forces = 0  # 필요한 특수소대의 수
    left, right = 0, N - 1  # 왼쪽과 오른쪽 포인터

    while left <= right:
        total_forces += 1  # 특수소대 1개 추가
        remaining_forces = W - enemies[right]  # 남은 특수소대의 수용 인원

        if enemies[left] <= remaining_forces:
            left += 1

        right -= 1

    return total_forces

import sys


input = sys.stdin.readline


# 테스트 케이스 입력
T = int(input())
for _ in range(T):
    N, W = map(int, input().strip().split())
    enemies1 = list(map(int, input().strip().split()))
    enemies2 = list(map(int, input().strip().split()))

    '''
    최소로 이뤄질수 있는 쌍
    위아래로 N개만큼 이뤄질 수 있음
    min = N
    여기서 경우가 나뉨
    양 옆으로 매칭 될 경우.
    위 아래로 매칭 될 경우.
    '''

    # 두 번째 줄의 입력을 첫 번째 줄에 이어붙임
    enemies = enemies1 + enemies2

    result = min_special_forces(2 * N, W, enemies)
    print(result)
