def solution(numbers):
    numbers.sort(key = lambda x : str(x)*3, reverse = True)
    return str(int(''.join(list(map(str, numbers)))))

### 메모
# 문자열 정렬 이용, 문자열 반복을 이용하여 우선순위 선정.
# lambda 사용 : [https://www.notion.so/Python-Counter-lambda-dbef39bd8058456a87de41ede5ffcb8c](https://www.notion.so/Python-Counter-lambda-dbef39bd8058456a87de41ede5ffcb8c)
# map 사용 : [https://www.notion.so/Python-map-db55623ed21c47cea3d0fb40fd132999](https://www.notion.so/Python-map-db55623ed21c47cea3d0fb40fd132999)

# 가장 큰 수
# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
# 입출력 예
# numbers	return
# [6, 10, 2]	"6210"
# [3, 30, 34, 5, 9]	"9534330"
# ※ 공지 - 2021년 10월 20일 테스트케이스가 추가되었습니다.