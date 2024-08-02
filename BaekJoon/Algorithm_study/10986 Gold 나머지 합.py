import sys


def count_subarrays_with_remainder(M, array):
    # 누적 합의 나머지를 저장할 카운터 배열
    remainder_count = [0] * M
    remainder_count[0] = 1  # 초기 상태를 위해 나머지 0인 경우 하나 추가
    
    prefix_sum = 0
    result = 0

    for num in array:
        prefix_sum += num
        remainder = prefix_sum % M
        
        # 이 나머지가 나온 적이 있는지 확인하고 결과에 추가
        result += remainder_count[remainder]
        
        # 현재 나머지 카운트를 증가
        remainder_count[remainder] += 1
    
    return result

# 입력
input = sys.stdin.readline
N, M = map(int, input().split())
array = list(map(int, input().split()))

# 결과 계산 및 출력
print(count_subarrays_with_remainder(M, array))

'''
### 문제 풀이

```python
import sys

def count_subarrays_with_remainder(M, array):
    # 누적 합의 나머지를 저장할 카운터 배열
    remainder_count = [0] * M
    remainder_count[0] = 1  # 초기 상태를 위해 나머지 0인 경우 하나 추가
    
    prefix_sum = 0
    result = 0

    for num in array:
        prefix_sum += num
        remainder = prefix_sum % M
        
        # 이 나머지가 나온 적이 있는지 확인하고 결과에 추가
        result += remainder_count[remainder]
        
        # 현재 나머지 카운트를 증가
        remainder_count[remainder] += 1
    
    return result

# 입력
input = sys.stdin.readline
N, M = map(int, input().split())
array = list(map(int, input().split()))

# 결과 계산 및 출력
print(count_subarrays_with_remainder(M, array))
```

# 나머지 합

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 53067 | 14816 | 10673 | 26.369% |

## 문제

수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.

즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

## 입력

첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)

둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)

## 출력

첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.

## 예제 입력 1

```
5 3
1 2 3 1 2

```

## 예제 출력 1

```
7

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [cs71107](https://www.acmicpc.net/user/cs71107)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [누적 합](https://www.acmicpc.net/problem/tag/139)

## 메모

누적으로 더하고 M 값으로 나눠지는 값이 나오면 그 값만큼 추가로 더해서 진행.
'''