# def solution(priorities, location):
#     answer = 0
#     loc = [i for i in range(len(priorities))]
#     final_loc = []
    
#     while priorities :
#         if priorities[0] == max(priorities):
#             final_loc.append(loc.pop(0))
#             priorities.pop(0)
#         else:
#             priorities.append(priorities.pop(0))
#             loc.append(loc.pop(0))
            
#     answer = final_loc.index(location) + 1
    
#     return answer

# from collections import deque

# def solution(priorities, location):
#     answer = 0
    
#     mark = []
#     mine = priorities[location]
    
#     for i, priority in enumerate(priorities):
#         mark.append((priority, i))
    
#     p = 0
    
#     while priorities:
#         if priorities[0] == max(priorities):
#             p += 1
#             priorities.pop(0)
        
#         else:
#             mark.append(mark.pop(p))
#             priorities.append(priorities.pop(0))
        
#     answer = mark.index((mine,location)) + 1
    
#     print(mark)
#     return answer

def solution(priorities, location):
    answer = 0
    
    mark = []
    
    for i, priority in enumerate(priorities):
        if i == location:
            mark.append((1, priority))
        else:
            mark.append((0,priority))
    
    num = 0
    while priorities:
        if priorities[0] == max(priorities) :
            num += 1
            priorities.pop(0)
            temp = mark.pop(0)
            if temp[0]:
                answer = num
                break
        else:
            priorities.append(priorities.pop(0))
            mark.append(mark.pop(0))
    
    return answer
