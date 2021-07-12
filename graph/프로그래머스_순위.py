def solution(n, results):
    answer = 0
    wins = [set() for _ in range(n)]
    loses = [set() for _ in range(n)]
    
    for winner, loser in results:
        wins[winner-1].add(loser-1)
        loses[loser-1].add(winner-1)
        
    for i in range(n):
        for winner in loses[i]:
            wins[winner].update(wins[i])        
        for loser in wins[i]:
            loses[loser].update(loses[i])    
    
    for i in range(n):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1
    
    return answer
