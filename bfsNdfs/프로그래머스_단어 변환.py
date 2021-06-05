def solution(begin, target, words):
    answer = 0
    
    stack = [begin]
    
    visited = {i:0 for i in words}
    
    if target not in words:
        return 0
    
    while stack:
        st = stack.pop()

        if st == target:
            return answer
        
        for word in words:
            for i in range(len(word)):
                copy = list(word)
                copy_front = list(st)
                copy[i] = 0
                copy_front[i] = 0
                
                if copy == copy_front:
                    if visited[word] != 0:
                        continue
                    visited[word] = 1
                    stack.append(word)
                    break
        answer += 1
    
    return answer
