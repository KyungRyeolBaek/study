import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
results = ['1' for _ in range(M)]
print(' '.join(results))
while results != [f'{N}' for _ in range(M)]:
    cur = -1
    results[cur] = str(int(results[cur]) + 1)
    while True:
        if results[cur] >= f'{N + 1}':
            if results[cur - 1] > f'{N}':
                results[cur] = str(int(results[cur - 1]))
            elif results[cur - 1] == f'{N}':
                i = 1
                while True:
                    if results[cur - 1 - i] == f'{N}':
                        i += 1
                    else:
                        results[cur] = str(int(results[cur - 1 - i]) + 1)
                        break
            else:
                results[cur] = str(int(results[cur - 1]) + 1)
            cur -= 1
            results[cur] = str(int(results[cur]) + 1)
        else:
            break
    print(' '.join(results))

'''
# N과 M (4)

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 512 MB | 58723 | 46232 | 36812 | 78.742% |

## 문제

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
    - 길이가 K인 수열 A가 A ≤ A ≤ ... ≤ A ≤ A를 만족하면, 비내림차순이라고 한다.
        
        1
        
        2
        
        K-1
        
        K
        

## 입력

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

## 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제 입력 1

```
3 1

```

## 예제 출력 1

```
1
2
3

```

## 예제 입력 2

```
4 2

```

## 예제 출력 2

```
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4

```

## 예제 입력 3

```
3 3

```

## 예제 출력 3

```
1 1 1
1 1 2
1 1 3
1 2 2
1 2 3
1 3 3
2 2 2
2 2 3
2 3 3
3 3 3

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [백트래킹](https://www.acmicpc.net/problem/tag/5)

## 메모

값을 하나씩 증가하면서 이전 값들보다 낮으면 같을 때까지 증가.
'''