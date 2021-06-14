def solution(answers):
    answer = []
    math1 = [1,2,3,4,5]
    math2 = [2,1,2,3,2,4,2,5]
    math3 = [3,3,1,1,2,2,4,4,5,5]
    res = [0,0,0]
    for i in range(len(answers)) : 
        if math1[i%len(math1)] == answers[i] :
            res[0] += 1
        if math2[i%len(math2)] == answers[i] :
            res[1] += 1
        if math3[i%len(math3)] == answers[i] :
            res[2] += 1    
    if res[0] == max(res) : 
        answer.append(1)
    if res[1] == max(res) : 
        answer.append(2)
    if res[2] == max(res) : 
        answer.append(3)    
    return answer
