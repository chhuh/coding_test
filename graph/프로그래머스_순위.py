def solution(n, results):
    answer = 0
    wins = {}
    loses = {}
    
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()
        
    for i in range(1, n+1):
        for a, b in results:
            if a == i:
                wins[i].add(b)
            if b == i:
                loses[i].add(a)
        
        for winner in loses[i]:
            wins[winner].update(wins[i])
        
        for loser in wins[i]:
            loses[loser].update(loses[i])
            
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1
    return answer
