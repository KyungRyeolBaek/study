from itertools import permutations

def check_id(user, banned):
    if len(user) != len(banned):
            return False
    for i in range(len(user)):
        if banned[i] != '*' and user[i] != banned[i]:
            return False
    
    return True

def solution(user_id, banned_id):
    answer = 0
    ban_list = []
    user_id_set = set()
    user_id_list = list(permutations(user_id, len(banned_id)))
    for user_list in user_id_list:
        for user, banned in zip(user_list, banned_id):
            if check_id(user, banned):
                continue
            else:
                break
        else:
            user_list = tuple(sorted(user_list))
            if user_list not in user_id_set:
                user_id_set.add(user_list)
                
    return len(user_id_set)


### 메모
# permutations 순열 : [Python 순열, 조합, product - itertools](https://www.notion.so/Python-product-itertools-1311c62b2ea94dd6b395471f37033fc8) 
# for else 문 : [Python for else문](https://www.notion.so/Python-for-else-f29c8d69a3c5461dbb0040f1e3d77b8e) 
# id를 검사 할 때 *이 아닐 때 문자가 같지 않으면 False 그 외엔 True 반환
# 모든 경우의 수에 부합하는 경우의 개수 출력
# 같은 아이디로 구성 되어 있는 경우는 포함하지 않는다.



# 불량 사용자
# 문제 설명
# 개발팀 내에서 이벤트 개발을 담당하고 있는 "무지"는 최근 진행된 카카오이모티콘 이벤트에 비정상적인 방법으로 당첨을 시도한 응모자들을 발견하였습니다. 이런 응모자들을 따로 모아 불량 사용자라는 이름으로 목록을 만들어서 당첨 처리 시 제외하도록 이벤트 당첨자 담당자인 "프로도" 에게 전달하려고 합니다. 이 때 개인정보 보호을 위해 사용자 아이디 중 일부 문자를 '*' 문자로 가려서 전달했습니다. 가리고자 하는 문자 하나에 '*' 문자 하나를 사용하였고 아이디 당 최소 하나 이상의 '*' 문자를 사용하였습니다.
# "무지"와 "프로도"는 불량 사용자 목록에 매핑된 응모자 아이디를 제재 아이디 라고 부르기로 하였습니다.

# 예를 들어, 이벤트에 응모한 전체 사용자 아이디 목록이 다음과 같다면

# 응모자 아이디
# frodo
# fradi
# crodo
# abc123
# frodoc
# 다음과 같이 불량 사용자 아이디 목록이 전달된 경우,

# 불량 사용자
# fr*d*
# abc1**
# 불량 사용자에 매핑되어 당첨에서 제외되어야 야 할 제재 아이디 목록은 다음과 같이 두 가지 경우가 있을 수 있습니다.

# 제재 아이디
# frodo
# abc123
# 제재 아이디
# fradi
# abc123
# 이벤트 응모자 아이디 목록이 담긴 배열 user_id와 불량 사용자 아이디 목록이 담긴 배열 banned_id가 매개변수로 주어질 때, 당첨에서 제외되어야 할 제재 아이디 목록은 몇가지 경우의 수가 가능한 지 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# user_id 배열의 크기는 1 이상 8 이하입니다.
# user_id 배열 각 원소들의 값은 길이가 1 이상 8 이하인 문자열입니다.
# 응모한 사용자 아이디들은 서로 중복되지 않습니다.
# 응모한 사용자 아이디는 알파벳 소문자와 숫자로만으로 구성되어 있습니다.
# banned_id 배열의 크기는 1 이상 user_id 배열의 크기 이하입니다.
# banned_id 배열 각 원소들의 값은 길이가 1 이상 8 이하인 문자열입니다.
# 불량 사용자 아이디는 알파벳 소문자와 숫자, 가리기 위한 문자 '*' 로만 이루어져 있습니다.
# 불량 사용자 아이디는 '*' 문자를 하나 이상 포함하고 있습니다.
# 불량 사용자 아이디 하나는 응모자 아이디 중 하나에 해당하고 같은 응모자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없습니다.
# 제재 아이디 목록들을 구했을 때 아이디들이 나열된 순서와 관계없이 아이디 목록의 내용이 동일하다면 같은 것으로 처리하여 하나로 세면 됩니다.
# [입출력 예]
# user_id	banned_id	result
# ["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "abc1**"]	2
# ["frodo", "fradi", "crodo", "abc123", "frodoc"]	["*rodo", "*rodo", "******"]	2
# ["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "*rodo", "******", "******"]	3
# 입출력 예에 대한 설명
# 입출력 예 #1
# 문제 설명과 같습니다.

# 입출력 예 #2
# 다음과 같이 두 가지 경우가 있습니다.

# 제재 아이디
# frodo
# crodo
# abc123
# 제재 아이디
# frodo
# crodo
# frodoc
# 입출력 예 #3
# 다음과 같이 세 가지 경우가 있습니다.

# 제재 아이디
# frodo
# crodo
# abc123
# frodoc
# 제재 아이디
# fradi
# crodo
# abc123
# frodoc
# 제재 아이디
# fradi
# frodo
# abc123
# frodoc