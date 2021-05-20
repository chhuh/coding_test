from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    worker = defaultdict(list)
    
    for i in info:
        i = i.split(" ")
        info_key = i[:-1]
        info_val = int(i[-1])
        
        for i in range(5):
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                worker[tmp_key].append(info_val)
                
    for w in worker.keys():
        worker[w].sort()
        
    for q in query:
        q = q.split(" and ")
        q.append(q[3].split(" ")[1])
        q[3] = q[3].split(" ")[0]       
        
        q_val = int(q[-1])
        q = q[:-1]
        
        while "-" in q:
            q.remove("-")
        temp_q = ''.join(q)
        
        if temp_q in worker:
            val = worker[temp_q]
            if len(val) > 0:
                start, end = 0, len(val)
                while end > start:
                    mid = (start + end) // 2
                    if val[mid] >= q_val:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(val)-start)
        else:
            answer.append(0)
    return answer
