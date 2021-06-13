def solution(citations):
    answer = 0
    l = len(citations)
    citations.sort()
    for i in range(l) :
        if (l - i) < citations[i] : 
            answer = l - i
            return answer
    return answer
