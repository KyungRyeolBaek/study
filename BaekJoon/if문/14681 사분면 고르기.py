a = int(input())
b = int(input())

def quadrant(a, b):
    if a*b > 0:
        if a > 0:
            return 1
        else:
            return 3
    elif a*b < 0:
        if a < 0:
            return 2
        else:
            return 4
    elif a*b == 0:
        print('error! a or b must not be 0')

print(quadrant(a, b))

# short
print('1243'['0'>input()::2]['0'>input()])

'''
문제
흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다. 사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다. "Quadrant n"은 "제n사분면"이라는 뜻이다.



예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.

점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.

입력
첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)

출력
점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.

예제 입력 1 
12
5
예제 출력 1 
1
예제 입력 2 
9
-13
예제 출력 2 
4
출처
Olympiad > Canadian Computing Competition & Olympiad > 2017 > CCC 2017 Junior Division 1번

문제를 번역한 사람: jh05013
알고리즘 분류
수학
구현
기하학
'''