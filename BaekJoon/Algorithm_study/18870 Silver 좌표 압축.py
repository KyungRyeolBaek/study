import sys


input = sys.stdin.readline
N = int(input())
answer = [0 for _ in range(N)]
mapping = {}
numbers = list(map(int, input().strip().split()))
for idx, number in enumerate(numbers):
    idx_list = mapping.get(number, [])
    idx_list.append(idx)
    mapping[number] = idx_list

numbers = list(set(numbers))
numbers.sort()
count = 0
for number in numbers:
    for idx in mapping[number]:
        answer[idx] = str(count)
    count += 1

print(' '.join(answer))

'''
# 좌표 압축

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 512 MB | 93910 | 39564 | 29723 | 39.489% |

## 문제

수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

## 입력

첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

## 출력

첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

## 제한

- 1 ≤ N ≤ 1,000,000
- 10 ≤ X ≤ 10
    
    9
    
    i
    
    9
    

## 예제 입력 1

```
5
2 4 -10 4 -9

```

## 예제 출력 1

```
2 3 0 3 1

```

## 예제 입력 2

```
6
1000 999 1000 999 1000 999

```

## 예제 출력 2

```
1 0 1 0 1 0

```

## 출처

- 문제의 오타를 찾은 사람: [abel1802](https://www.acmicpc.net/user/abel1802)
- 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [정렬](https://www.acmicpc.net/problem/tag/97)
- [값 / 좌표 압축](https://www.acmicpc.net/problem/tag/161)

## 메모

[Python dict key, value 추가 딕셔너리 원소 추가](https://www.notion.so/Python-dict-key-value-e1405c8ff17a46a19d2078eccb33cdda?pvs=21)

mapping 해서 안하면 시간 제한 걸림.

넣어야 하는 값들만 맵핑해서 idx 넣어놓고

중복 제거 한 후 정렬해서 하나씩 idx 뽑아서 그 위치에 값을 오름차순으로 넣으면 됨.
'''