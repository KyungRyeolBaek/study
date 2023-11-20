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

# 테스트 케이스 입력
T = int(input())
for _ in range(T):
    N, W = map(int, input().strip().split())
    enemies1 = list(map(int, input().strip().split()))
    enemies2 = list(map(int, input().strip().split()))

    # 두 번째 줄의 입력을 첫 번째 줄에 이어붙임
    enemies = enemies1 + enemies2

    result = min_special_forces(2 * N, W, enemies)
    print(result)
