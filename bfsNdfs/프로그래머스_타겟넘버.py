# bfs

from collections import deque

def solution(numbers, target):
    answer = 0
    stack = deque([(0,0)])
    
    while stack:
        cur_sum, num_idx = stack.popleft()
        
        if num_idx == len(numbers):
            if cur_sum == target:
                answer += 1
        
        else:
            stack.append((cur_sum + numbers[num_idx], num_idx + 1))
            stack.append((cur_sum - numbers[num_idx], num_idx + 1))
    
    return answer
