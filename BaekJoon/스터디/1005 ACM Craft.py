import sys
from collections import deque


input = sys.stdin.readline

# T: 테스트 케이스
# N, K: 건물 개수, 건물 순서 규칙 총 개수
# D: 걸리는 시간
# X, Y: 건물 순서.
T = int(input())
for _ in range(T):
    N, K = map(int, input().strip().split())
    D = list(map(int, input().strip().split()))
    G = [[] for _ in range(N + 1)]
    require_building_count = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().strip().split())
        G[X].append(Y)
        require_building_count[Y] += 1
    W = int(input())

    # 건물을 짓는데 걸리는 최소 시간을 저장하는 배열
    time_to_build = [0] * (N + 1)

    # 짓기 시작할 건물을 큐에 추가
    que = deque([])
    for i in range(1, N + 1):
        if require_building_count[i] == 0:
            que.append(i)
            time_to_build[i] = D[i - 1]

    while que:
        current_building = que.popleft()
        if current_building == W:
            print(time_to_build[current_building])
            break
        for next_building in G[current_building]:
            require_building_count[next_building] -= 1
            # 소요 시간 최대값으로.
            time_to_build[next_building] = max(time_to_build[next_building], time_to_build[current_building] + D[next_building - 1])
            if require_building_count[next_building] == 0:
                que.append(next_building)


'''
## 문제

서기 2012년! 드디어 2년간 수많은 국민들을 기다리게 한 게임 ACM Craft (Association of Construction Manager Craft)가 발매되었다.

이 게임은 지금까지 나온 게임들과는 다르게 ACM크래프트는 다이나믹한 게임 진행을 위해 건물을 짓는 순서가 정해져 있지 않다. 즉, 첫 번째 게임과 두 번째 게임이 건물을 짓는 순서가 다를 수도 있다. 매 게임시작 시 건물을 짓는 순서가 주어진다. 또한 모든 건물은 각각 건설을 시작하여 완성이 될 때까지 Delay가 존재한다.

!https://www.acmicpc.net/upload/201003/star.JPG

위의 예시를 보자.

이번 게임에서는 다음과 같이 건설 순서 규칙이 주어졌다. 1번 건물의 건설이 완료된다면 2번과 3번의 건설을 시작할수 있다. (동시에 진행이 가능하다) 그리고 4번 건물을 짓기 위해서는 2번과 3번 건물이 모두 건설 완료되어야지만 4번건물의 건설을 시작할수 있다.

따라서 4번건물의 건설을 완료하기 위해서는 우선 처음 1번 건물을 건설하는데 10초가 소요된다. 그리고 2번 건물과 3번 건물을 동시에 건설하기 시작하면 2번은 1초뒤에 건설이 완료되지만 아직 3번 건물이 완료되지 않았으므로 4번 건물을 건설할 수 없다. 3번 건물이 완성되고 나면 그때 4번 건물을 지을수 있으므로 4번 건물이 완성되기까지는 총 120초가 소요된다.

프로게이머 최백준은 애인과의 데이트 비용을 마련하기 위해 서강대학교배 ACM크래프트 대회에 참가했다! 최백준은 화려한 컨트롤 실력을 가지고 있기 때문에 모든 경기에서 특정 건물만 짓는다면 무조건 게임에서 이길 수 있다. 그러나 매 게임마다 특정건물을 짓기 위한 순서가 달라지므로 최백준은 좌절하고 있었다. 백준이를 위해 특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내는 프로그램을 작성해주자.

## 입력

첫째 줄에는 테스트케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 주어진다. 첫째 줄에 건물의 개수 N과 건물간의 건설순서 규칙의 총 개수 K이 주어진다. (건물의 번호는 1번부터 N번까지 존재한다)

둘째 줄에는 각 건물당 건설에 걸리는 시간 D1, D2, ..., DN이 공백을 사이로 주어진다. 셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. (이는 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미이다)

마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다.

## 출력

건물 W를 건설완료 하는데 드는 최소 시간을 출력한다. 편의상 건물을 짓는 명령을 내리는 데는 시간이 소요되지 않는다고 가정한다.

건설순서는 모든 건물이 건설 가능하도록 주어진다.

## 제한

- 2 ≤ N ≤ 1000
- 1 ≤ K ≤ 100,000
- 1 ≤ X, Y, W ≤ N
- 0 ≤ D ≤ 100,000, D는 정수
    
    i
    
    i
    

## 예제 입력 1

```
2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7

```

## 예제 출력 1

```
120
39

```

## 예제 입력 2

```
5
3 2
1 2 3
3 2
2 1
1
4 3
5 5 5 5
1 2
1 3
2 3
4
5 10
100000 99999 99997 99994 99990
4 5
3 5
3 4
2 5
2 4
2 3
1 5
1 4
1 3
1 2
4
4 3
1 1 1 1
1 2
3 2
1 4
4
7 8
0 0 0 0 0 0 0
1 2
1 3
2 4
3 4
4 5
4 6
5 7
6 7
7

```

## 예제 출력 2

```
6
5
399990
2
0

```

## 출처

- 잘못된 조건을 찾은 사람: [annaria](https://www.acmicpc.net/user/annaria)
- 문제를 만든 사람: [author1](https://www.acmicpc.net/user/author1)
- 데이터를 추가한 사람: [djm03178](https://www.acmicpc.net/user/djm03178), [doju](https://www.acmicpc.net/user/doju), [minshogi](https://www.acmicpc.net/user/minshogi), [zzaa9898](https://www.acmicpc.net/user/zzaa9898)
- 어색한 표현을 찾은 사람: [gorisanson](https://www.acmicpc.net/user/gorisanson)
- 잘못된 데이터를 찾은 사람: [tncks0121](https://www.acmicpc.net/user/tncks0121)
- 문제의 오타를 찾은 사람: [xivnick](https://www.acmicpc.net/user/xivnick)
- 빠진 조건을 찾은 사람: [yclock](https://www.acmicpc.net/user/yclock)

## 알고리즘 분류

- [다이나믹 프로그래밍](https://www.acmicpc.net/problem/tag/25)
- [그래프 이론](https://www.acmicpc.net/problem/tag/7)
- [위상 정렬](https://www.acmicpc.net/problem/tag/78)
- [방향 비순환 그래프](https://www.acmicpc.net/problem/tag/213)

## 메모

위상 정렬 사용해서 풀어야 함.

하나 하나씩 순서대로 구현 하면 됨.

1. 초기에 시작할 건물을 큐에 추가.
    1. 필요한 이전 건물이 없는 건물 먼저 시작.
    2. 소요된 시간 리스트에 추가.
2. 큐에서 꺼내온 건물 번호로 시작
    1. 건물 번호가 W와 일치하면 
        1. 소요된 시간 출력.
    2. 다음 건물 번호를 불러와서
        1. 소요시간 최대값으로 갱신.
            1. 필요한 이전 건물이 다 지어지면 que에 다음 건물들 추가.

[위상 정렬](https://www.notion.so/f9ce0227e7514cc69c5d98f7a565ecfd?pvs=21)
'''