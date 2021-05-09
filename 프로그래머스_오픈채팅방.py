def solution(record):
    answer = []
    temp = []
    hash = {}
    for rec in record:
        r = rec.split(" ")
        if r[1] not in hash.keys():
            hash[r[1]] = r[2]
        elif r[1] in hash.keys() and r[0] != "Leave":
            hash[r[1]] = r[2]
        else:
            pass
    
    for rec in record:
        r = rec.split(" ")
        if r[0] == "Enter":
            answer.append(str(hash[r[1]]) + "님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(str(hash[r[1]]) + "님이 나갔습니다.")
        else:
            pass
    return answer
