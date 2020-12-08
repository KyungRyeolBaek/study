def solution(N, stages):
    total_failture_rate = {}
    for i in range(N):
        stage_fail = 0
        stage_total = 0
        failture_rate = 0
        for j in stages:
            if j == (i+1):
                stage_fail += 1
            elif j > (i+1):
                stage_total += 1
        stage_total = stage_total + stage_fail
        failture_rate = stage_fail / stage_total
        total_failture_rate[i+1] = failture_rate
    return [i[0] for i in sorted(total_failture_rate.items(), key = lambda item:item[1], reverse = True)]
