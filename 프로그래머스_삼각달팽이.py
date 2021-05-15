def solution(n):
    answer = []
    
    snail = [[0]*i for i in range(1, n+1)]
    max_cnt = sum(range(1, n+1))
    
    three = 0
    cnt = 0
    
    while cnt != max_cnt:
        if three % 3 == 0:
            for i in range((three//3)*2, n-(three//3)):
                cnt += 1
                snail[i][three//3] = cnt
            three += 1
            
        elif three % 3 == 1:
            for i in range((three//3)+1, n-(three//3)*2):
                cnt += 1
                snail[n-1-(three//3)][i] = cnt
            three += 1

        else:
            for i in range((three//3) + 2, n-(three//3)*2):
                cnt += 1
                snail[n-i][-1-(three//3)] = cnt
            three += 1
    
    for sn in snail:
        for s in sn:
            answer.append(s)
    return answer
