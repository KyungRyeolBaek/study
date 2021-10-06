S = input().upper()
C = set(S)
res = {i : S.count(i) for i in C}
sorted_res = sorted(res.items(), key=lambda x: x[1], reverse=True)

if sorted_res[0][1] == sorted_res[1][1]:
    print('?')
else:
    print(sorted_res[0][0])

# short
from statistics import*
try:t=mode(input().upper())
except:t='?'
print(t)

'''
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1 
Mississipi
예제 출력 1 
?
예제 입력 2 
zZa
예제 출력 2 
Z
예제 입력 3 
z
예제 출력 3 
Z
예제 입력 4 
baaa
예제 출력 4 
A
출처
문제를 만든 사람: author5
데이터를 추가한 사람: jh05013
알고리즘 분류
구현
문자열
'''