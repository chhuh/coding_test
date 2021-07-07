from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    release_date = []
    
    for i in range(0, len(progresses)):
        release_date.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    deque_release_date = deque(release_date)    
    max = 0
    num = 1
    
    while deque_release_date:
        temp = deque_release_date.popleft()
        if(max < temp):
            if max == 0:
                max = temp
            else:
                max = temp
                answer.append(num)
                num = 1
        else:
            num += 1
            
    answer.append(num)
    
    return answer
