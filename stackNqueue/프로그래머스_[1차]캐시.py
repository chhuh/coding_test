def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5*len(cities)
    
    answer = 0
    lower_cities = [i.lower() for i in cities]
    
    
    queue = ["Default"]*cacheSize
    
    for lc in lower_cities:
        if lc in queue:
            queue.remove(lc)
            queue.append(lc)
            answer += 1
        else:
            queue.pop(0)
            queue.append(lc)
            answer += 5
    
    return answer
