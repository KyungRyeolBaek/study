def solution(n):
    return int(''.join(reversed(sorted([i for i in str(n)]))))

# sorted(a) a를 오름차순으로 나열
# reversed(a) a를 역순으로 나열
# reversed를 썼을때 ''.join 이나 map으로 묶어줘야됨
# list(map(int, a)) a를 int로 나열, map을 쓸 경우 list


# 문제 설명
# 함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

# 제한 조건
# n은 1이상 8000000000 이하인 자연수입니다.
# 입출력 예
# n	return
# 118372	873211
