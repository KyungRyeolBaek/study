def solution(numbers):
    return sorted(list(set([a + b for i, a in enumerate(numbers) for j, b in enumerate(numbers) if i != j])))
## 2중 for문에 if문 추가, else 추가 안할시 if문은 for문 뒤로
## enumerate 리스트 idx 비교로 사용
## set 같은 원소 제거
## list로 변환
## sorted 정렬
