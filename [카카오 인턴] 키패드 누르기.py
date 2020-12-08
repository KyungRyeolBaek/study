def solution(numbers, hand):
    left_number =   [1, 4, 7, '*']
    middle_number = [2, 5, 8, 0]
    right_number =  [3, 6, 9, '#']
    answer = ''
    l_front_number = '*'
    r_front_number = '#'
    distance = [left_number,
               middle_number,
               right_number]
    n_r = -1
    l_r = 4
    r_r = 4
    n_c = -1
    l_c = 1
    r_c = 3
    
    for num in numbers:
        if num in left_number:
            answer += 'L'
            l_front_number = num
        elif num in right_number:
            answer += 'R'
            r_front_number = num
        elif num in middle_number:
            for i in range(3):
                for j in range(4):
                    if distance[i][j] == num:
                        n_r = j+1
                        n_c = i+1
                    elif distance[i][j] == l_front_number:
                        l_r = j+1
                        l_c = i+1
                    elif distance[i][j] == r_front_number:
                        r_r = j+1
                        r_c = i+1
            if ((l_r-n_r)**2) + ((l_c-n_c)**2) == ((r_r-n_r)**2 + (r_c-n_c)**2):
                if hand == 'right':
                    answer += 'R'
                    r_front_number = num
                elif hand == 'left':
                    answer += 'L'
                    l_front_number = num
            elif ((l_r-n_r)**2) + ((l_c-n_c)**2) > ((r_r-n_r)**2 + (r_c-n_c)**2):
                answer += 'R'
                r_front_number = num
            elif ((l_r-n_r)**2) + ((l_c-n_c)**2) < ((r_r-n_r)**2 + (r_c-n_c)**2):
                answer += 'L'
                l_front_number = num
    return answer
