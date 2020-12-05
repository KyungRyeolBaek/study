def solution(board, moves):
    # board =
    # [[0,0,0,0,0],
    #  [0,0,1,0,3],
    #  [0,2,5,0,1],
    #  [4,2,4,4,2],
    #  [3,5,1,3,1]]
    # moves =
    # [1,5,3,5,1,2,1,4]
    case = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                pass
            else:
                case.append(board[j][i-1])
                board[j][i-1] = 0
                if len(case) >= 2:
                    if case[len(case)-2] == case[len(case)-1]:
                        answer += 2
                        print(case)
                        del case[len(case)-2:len(case)]
                        print(case)
                        break
                    else:
                        pass
                else:
                    pass
                break
    return answer
