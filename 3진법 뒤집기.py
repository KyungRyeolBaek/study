def solution(n):
    def div_3(n):
        a,b = divmod(n,3)
        if a == 0:
            return str(b)
        else:
            return div_3(a) + str(b)
    return int(div_3(n)[::-1], base = 3)
## divmod 몫과 나머지를 추출해줌
## list[::-1] 역순으로 전부 출력
