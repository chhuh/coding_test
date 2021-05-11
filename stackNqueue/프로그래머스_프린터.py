def solution(priorities, location):
    answer = 0
    loc = [i for i in range(len(priorities))]
    final_loc = []
    
    while priorities :
        if priorities[0] == max(priorities):
            final_loc.append(loc.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
            
    answer = final_loc.index(location) + 1
    
    return answer
