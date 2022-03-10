def solution(name):
    answer = 0
    min_move = 0
    for idx, a in enumerate(name):  # 우 이동 최소값 최소 이동에 저장
        if not a == 'A':
            min_move = idx
    
    for idx, n in enumerate(name):
        answer += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)     # 상, 하 최소
        
        # 다음 idx의 값이 A가 나왔을 때 A가 아닌 다음 문자열 까지의 idx
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
            
        # 최소 이동, 좌 이동 비교, 좌로 갔다 우로 다시탐색 할 경우 총 3가지 비교
        min_move = min(min_move, 2*idx + len(name) - next_idx, 2*(len(name) - 1 - next_idx) + 2 + idx)      
    
    answer += min_move  # 좌, 우 이동 최소
    
    return answer

# 좌, 우, 좌 불가 각 구간 별로 탐색 진행 해야 할 듯.
### 메모
# 오른쪽 끝 부터 시작하는게 더 빠른 경우도 탐색 해야 함.
# enumerate : idx, 값을 반복문을 통해 출력


### 잘못 푼 풀이
def solution(name):
    answer = 0
    name = name.replace('A', 'a')
    idx = 0
    d = 1   # 탐색 방향 1, -1
    m = len(name)
    while not name.islower():
        c = name[idx%m]
        if c != 'a':
            answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)     # 상, 하 최소
            name = list(name)
            name[idx%m] = 'a'
            name = ''.join(name)
        # print(name, answer)
        
        if not name.islower():
            pass
        else:
            break
            
        next_idx = idx + d
        if name[next_idx%m] == 'a':
            pos_idx = idx
            pos_mov = 0
            neg_idx = idx
            neg_mov = 0
            while name[pos_idx%m] == 'a':
                pos_idx += d
                pos_mov += 1
            while name[neg_idx%m] == 'a':
                neg_idx += (-1)*d
                neg_mov += 1
            # print(pos_idx, pos_mov, neg_idx, neg_mov)
            if pos_mov <= neg_mov:
                idx = pos_idx
                answer += pos_mov
                continue
            else:
                d = (-1)*d
                idx = neg_idx
                answer += neg_mov
                continue
        
        idx += d
        answer += 1
            
    return answer
            
# "BBABAAAABBBAAAABABB" 26
# "BBAAAAAABBBAAAAAABB" 20
# "BBBAAAAAAAB" 8        < 이게 문제.
# "ABAAAAAAAAABB" 7
# "BBAABB" 8
# "BBBAAAAABAAAAAAAAAAA" 12
# "BAAAAAAAAAABAAAAAABB" 13
# "AAABBAB" 7            
# 오른쪽 끝을 먼저 들렸다 오는게 더 빠를 경우.

### 메모
# 오른쪽을 먼저 들리는 경우를 추가하기 힘듦.
# islower() : [https://www.notion.so/Python-isalpha-lower-replace-re-sub-swapcase-042fb3e5f4b841b7a35af2c9847d8ace](https://www.notion.so/Python-isalpha-lower-replace-re-sub-swapcase-042fb3e5f4b841b7a35af2c9847d8ace)


# 조이스틱
# 문제 설명
# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.

# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)
# 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
# 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

# 제한 사항
# name은 알파벳 대문자로만 이루어져 있습니다.
# name의 길이는 1 이상 20 이하입니다.
# 입출력 예
# name	return
# "JEROEN"	56
# "JAN"	23
# 출처

# ※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.
# ※ 공지 - 2022년 1월 14일 지문 수정 및 테스트케이스가 추가되었습니다. 이로 인해 이전에 통과하던 코드가 더 이상 통과하지 않을 수 있습니다.