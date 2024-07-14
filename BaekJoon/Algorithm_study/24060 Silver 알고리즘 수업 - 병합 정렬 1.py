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
            self.count += 1
        while i < len(left):
            sorted_list.append(left[i])
            i += 1
            self.count += 1
        while j < len(right):
            sorted_list.append(right[j])
            j += 1
            self.count += 1
        if self.count == self.k:
            self.result = sorted_list[-1]
        return sorted_list

input = sys.stdin.readline
size, K = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

Merge_Sort_ = Merge_Sort(K)
Merge_Sort_.merge_sort(A)
if Merge_Sort_.result != 0:
    print(Merge_Sort_.result)
else:
    print(-1)

