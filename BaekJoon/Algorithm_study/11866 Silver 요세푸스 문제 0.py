import sys


input = sys.stdin.readline
N, K = map(int, input().strip().split())
nums = [n for n in range(1, N + 1)]
pop_list = []
pos = 0
while len(nums) != 0:
    if pos >= 0:
        pos = (pos + K) % len(nums) - 1
    else:
        pos = (pos + K) % len(nums)
    pop_list.append(str(nums[pos]))
    del nums[pos]
print(f"<{', '.join(pop_list)}>")

'''
# 요세푸스 문제 0

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 512 MB | 80744 | 45824 | 38370 | 56.491% |

## 문제

요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

## 출력

예제와 같이 요세푸스 순열을 출력한다.

## 예제 입력 1

```
7 3

```

## 예제 출력 1

```
<3, 6, 2, 7, 5, 1, 4>

```

## 출처

- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)
- [자료 구조](https://www.acmicpc.net/problem/tag/175)
- [큐](https://www.acmicpc.net/problem/tag/72)

## 메모

마지막 숫자를 뽑아 냈을 때는 0번 위치 부터 다시 돌아야 함.

“, ‘ 프린트 할 때 주의
'''