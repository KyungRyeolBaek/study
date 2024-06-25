import sys
from collections import Counter


input = sys.stdin.readline
N = int(input())
nums = []
for _ in range(N):
    num = int(input().strip())
    nums.append(num)

print(int(round(sum(nums) / N, 0)))
print(sorted(nums)[N // 2])
counters = Counter(nums).most_common()
sorted_counters = sorted([num for num, count in counters if count == counters[0][1]])
if len(sorted_counters) == 1:
    print(sorted_counters[0])
else:
    print(sorted_counters[1])
print(max(nums) - min(nums))

'''
# 통계학

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 256 MB | 168891 | 41607 | 33290 | 26.599% |

## 문제

수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

## 출력

첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.

## 예제 입력 1

```
5
1
3
8
-2
2

```

## 예제 출력 1

```
2
2
1
10

```

## 예제 입력 2

```
1
4000

```

## 예제 출력 2

```
4000
4000
4000
0

```

## 예제 입력 3

```
5
-1
-2
-3
-1
-2

```

## 예제 출력 3

```
-2
-2
-1
2

```

## 예제 입력 4

```
3
0
0
-1

```

## 예제 출력 4

```
0
0
0
1

```

(0 + 0 + (-1)) / 3 = -0.333333... 이고 이를 첫째 자리에서 반올림하면 0이다. -0으로 출력하면 안된다.

## 출처

- 데이터를 추가한 사람: [bjh3502](https://www.acmicpc.net/user/bjh3502), [bsyun0571](https://www.acmicpc.net/user/bsyun0571), [djm03178](https://www.acmicpc.net/user/djm03178), [jungyh1509](https://www.acmicpc.net/user/jungyh1509), [kongum](https://www.acmicpc.net/user/kongum), [palilo](https://www.acmicpc.net/user/palilo), [YunGoon](https://www.acmicpc.net/user/YunGoon)
- 문제의 오타를 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013), [skynet](https://www.acmicpc.net/user/skynet)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)
- [정렬](https://www.acmicpc.net/problem/tag/97)

## 메모

최빈값은 collections의 Counter 함수를 사용 할 수 있다.

최빈값이 여러개 일 경우 가장 작은 두번째 값 출력 해야함.

[Python 교집합, 합집합, Counter, lambda](https://www.notion.so/Python-Counter-lambda-dbef39bd8058456a87de41ede5ffcb8c?pvs=21)
'''
