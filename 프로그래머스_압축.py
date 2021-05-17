def solution(msg):
    answer = []
    my_dict = dict()
    
    for i in range(26):
        my_dict[chr(65+i)] = i+1
    
    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg) : 
            answer.append(my_dict[msg[w:c]])
            break
        if msg[w:c+1] not in my_dict :
            my_dict[msg[w:c+1]] = len(my_dict) + 1
            answer.append(my_dict[msg[w:c]])
            w=c
    return answer
