for i in range(int(input())):
    print('{}'.format(i+1))

for i in range(int(input())):
    print(-~i)

# short -> unpacking 사용
print(*range(1,int(input())+1))

'''
문제
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

예제 입력 1 
5
예제 출력 1 
1
2
3
4
5
출처
문제를 만든 사람: baekjoon
잘못된 데이터를 찾은 사람: rory143
비슷한 문제
2742번. 기찍 N
알고리즘 분류
구현
'''