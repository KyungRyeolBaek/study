def solution(babbling):
    answer = 0
    ele = ['aya', 'ye', 'woo', 'ma']
    for b in babbling:
        tmp = 0
        for e in ele:
            idx = b.find(e)
            if idx == -1:
                continue
            else:
                tmp += len(e)
        
        if len(b) == tmp:
            answer += 1
            
    return answer

### 메모
# 단어 내에 찾는 원소가 있으면 원소의 글자수 만큼 tmp에 더한다.
# tmp와 단어의 길이가 같으면 answer를 1개씩 늘린다.

### 문제 설명
# 옹알이 (1)
# 문제 설명
# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한 발음밖에 하지 못합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ babbling의 길이 ≤ 100
# 1 ≤ babbling[i]의 길이 ≤ 15
# babbling의 원소는 "aya", "ye", "woo", "ma" 를 각각 최대 한 번씩만 포함합니다.
# 문자열은 알파벳 소문자로만 이루어져 있습니다.
# 입출력 예
# babbling	result
# ["aya", "yee", "u", "maa", "wyeoo"]	1
# ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]	3
# 입출력 예 설명
# 입출력 예 #1

# ["aya", "yee", "u", "maa", "wyeoo"]에서 발음할 수 있는 것은 "aya"뿐입니다. 따라서 1을 return합니다.
# 입출력 예 #2

# ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]에서 발음할 수 있는 것은 "aya" + "ye" = "ayaye", "ye", "ye" + "ma" + "woo" = "yemawoo"로 3개입니다. 따라서 2를 return합니다.
# 유의사항
# 네 가지를 붙여 만들 수 있는 발음 이외에는 어떤 발음도 할 수 없는 것으로 규정합니다. 예를 들어 "woowo"는 "woo"는 발음할 수 있지만 "wo"를 발음할 수 없기 때문에 할 수 없는 발음입니다.
# ※ 공지 - 2022년 10월 27일 문제 지문이 리뉴얼되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.