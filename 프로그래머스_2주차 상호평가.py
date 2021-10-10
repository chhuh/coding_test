import copy

def grade(s):
    if s>= 90:
        return "A"
    elif s>= 80 and s<90:
        return "B"
    elif s>= 70 and s<80:
        return "C"
    elif s>= 50 and s<70:
        return "D"
    else:
        return "F"

def solution(scores):
    answer = []
    
    student_num = len(scores)
    
    temp_scores = copy.deepcopy(scores)
    
    for i in range(student_num):
        for j in range(student_num):
            scores[i][j] = temp_scores[j][i]
    
    for i, score in enumerate(scores):
        if score[i] == min(score):
            temp = min(score)
            temp_min = copy.deepcopy(score)
            temp_min.remove(temp)
            if temp not in temp_min:
                answer.append(grade(sum(temp_min)/len(temp_min)))
            else:
                answer.append(grade(sum(score)/len(score)))
        elif score[i] == max(score):
            temp = max(score)
            temp_max = copy.deepcopy(score)
            temp_max.remove(temp)
            if temp not in temp_max:
                answer.append(grade(sum(temp_max)/len(temp_max)))
            else:
                answer.append(grade(sum(score)/len(score)))
        else:
            answer.append(grade(sum(score)/len(score)))
    
    return ''.join(answer)
