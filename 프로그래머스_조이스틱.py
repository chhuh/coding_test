def solution(name):
    answer = 0
    i = 0
    name = list(name)
    default = ["A"] * len(name)
    while(True) : 
        if name[i] != "A" : 
            answer += min(ord(name[i])-ord("A"), ord("Z") - ord(name[i]) + 1)
            name[i] = "A"
        if name == default :
            break
            
        r_cmd = 1
        l_cmd = 1
        while(name[i+r_cmd] == "A"):
            r_cmd += 1
        while(name[i-l_cmd] == "A"): 
            l_cmd += 1
    
        if r_cmd > l_cmd :
            answer += l_cmd
            i -= l_cmd
            
        else :
            answer += r_cmd
            i += r_cmd
    return answer
