''' pseudo code
merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
    if (p < r) then {
        q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
        merge_sort(A, p, q);      # 전반부 정렬
        merge_sort(A, q + 1, r);  # 후반부 정렬
        merge(A, p, q, r);        # 병합
    }
}

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
merge(A[], p, q, r) {
    i <- p; j <- q + 1; t <- 1;
    while (i ≤ q and j ≤ r) {
        if (A[i] ≤ A[j])
        then tmp[t++] <- A[i++]; # tmp[t] <- A[i]; t++; i++;
        else tmp[t++] <- A[j++]; # tmp[t] <- A[j]; t++; j++;
    }
    while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
        tmp[t++] <- A[i++];
    while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
        tmp[t++] <- A[j++];
    i <- p; t <- 1;
    while (i ≤ r)  # 결과를 A[p..r]에 저장
        A[i++] <- tmp[t++]; 
}
'''
import sys


class Merge_Sort:
    def __init__(self, k):
        self.count = 0
        self.k = k
        self.result = 0

    def merge_sort(self, unsorted_list):
        # 크기가 1이하면 반환
        if len(unsorted_list) <= 1:
            return unsorted_list
        
        # 리스트를 2분할
        mid = len(unsorted_list) // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]
        
        # 2분할한 리스트를 각각 merge sort진행
        left_ = self.merge_sort(left)
        right_ = self.merge_sort(right)
        return self.merge(left_, right_)

    def merge(self, left, right):
        i, j = 0,0
        sorted_list = []
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
            self.save_result(sorted_list)

        while i < len(left):
            sorted_list.append(left[i])
            i += 1
            self.save_result(sorted_list)

        while j < len(right):
            sorted_list.append(right[j])
            j += 1
            self.save_result(sorted_list)
            
        return sorted_list
    
    def save_result(self, sorted_list):
        self.count += 1
        if self.count == self.k:
            self.result = sorted_list[-1]


input = sys.stdin.readline
size, K = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

Merge_Sort_ = Merge_Sort(K)
Merge_Sort_.merge_sort(A)
if Merge_Sort_.result != 0:
    print(Merge_Sort_.result)
else:
    print(-1)

'''
# 알고리즘 수업 - 병합 정렬 1

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 512 MB | 17084 | 7744 | 6322 | 45.709% |

## 문제

오늘도 서준이는 병합 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

*N*개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 *K* 번째 저장되는 수를 구해서 우리 서준이를 도와주자.

크기가 *N*인 배열에 대한 병합 정렬 의사 코드는 다음과 같다.

```
merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
    if (p < r) then {
        q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
        merge_sort(A, p, q);      # 전반부 정렬
        merge_sort(A, q + 1, r);  # 후반부 정렬
        merge(A, p, q, r);        # 병합
    }
}

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
merge(A[], p, q, r) {
    i <- p; j <- q + 1; t <- 1;
    while (i ≤ q and j ≤ r) {
        if (A[i] ≤ A[j])
        then tmp[t++] <- A[i++]; # tmp[t] <- A[i]; t++; i++;
        else tmp[t++] <- A[j++]; # tmp[t] <- A[j]; t++; j++;
    }
    while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
        tmp[t++] <- A[i++];
    while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
        tmp[t++] <- A[j++];
    i <- p; t <- 1;
    while (i ≤ r)  # 결과를 A[p..r]에 저장
        A[i++] <- tmp[t++];
}
```

## 입력

첫째 줄에 배열 A의 크기 *N*(5 ≤ *N* ≤ 500,000), 저장 횟수 *K*(1 ≤ *K* ≤ 108)가 주어진다.

다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

## 출력

배열 A에 *K* 번째 저장 되는 수를 출력한다. 저장 횟수가 *K* 보다 작으면 -1을 출력한다.

## 예제 입력 1

```
5 7
4 5 1 3 2

```

## 예제 출력 1

```
3

```

4 5 1 3 2 -> **4** 5 1 3 2 -> 4 **5** 1 3 2 -> **1** 5 1 3 2 -> 1 **4** 1 3 2 -> 1 4 **5** 3 2 -> 1 4 5 **2** 2 -> 1 4 5 2 **3** -> **1** 4 5 2 3 -> 1 **2** 5 2 3 -> 1 2 **3** 2 3 -> 1 2 3 **4** 3 -> 1 2 3 4 **5**. 총 12회 저장이 발생하고 일곱 번째 저장되는 수는 3이다.

## 예제 입력 2

```
5 13
4 5 1 3 2

```

## 예제 출력 2

```
-1

```

저장 횟수 12가 *K* 보다 작으므로 -1을 출력한다.

## 출처

- 문제를 검수한 사람: [chansol](https://www.acmicpc.net/user/chansol), [eric00513](https://www.acmicpc.net/user/eric00513), [jhnah917](https://www.acmicpc.net/user/jhnah917), [jthis](https://www.acmicpc.net/user/jthis), [kdh6429](https://www.acmicpc.net/user/kdh6429), [parkky](https://www.acmicpc.net/user/parkky), [tony9402](https://www.acmicpc.net/user/tony9402)
- 문제를 만든 사람: [MenOfPassion](https://www.acmicpc.net/user/MenOfPassion)

## 알고리즘 분류

- [구현](https://www.acmicpc.net/problem/tag/102)
- [정렬](https://www.acmicpc.net/problem/tag/97)
- [재귀](https://www.acmicpc.net/problem/tag/62)

## 메모

[병합 정렬 Merge Sort](https://www.notion.so/Merge-Sort-634c6f12fb72410bb2f765c9a897b0b4?pvs=21) 

병합 정렬을 이용하여 풀이.

class 형태로 구현하여 문제 풀이.
'''