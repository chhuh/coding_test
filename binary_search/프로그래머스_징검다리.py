def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    
    left = 0
    right = distance
    
    while left <= right:
        mid = (left + right) // 2
        
        del_stones = 0
        pre_stone = 0
        
        for rock in rocks:
            if rock - pre_stone < mid :
                del_stones += 1
            else:
                pre_stone = rock
            
            if del_stones >n :
                break
        
        if del_stones >n:
            # answer = mid
            right = mid - 1
            
        else:
            answer = mid
            left = mid + 1
        
    return answer
