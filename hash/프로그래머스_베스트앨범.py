def solution(genres, plays):
    answer = []
    
    my_genre = {}
    
    for i, genre in enumerate(genres):
        if genre in my_genre:
            temp = my_genre[genre][0] + plays[i]
            del my_genre[genre][0]
            my_genre[genre].append((i, plays[i]))
            my_genre[genre].sort(key = lambda x : (-x[1], x[0]))
            my_genre[genre].insert(0, temp)
        else:
            my_genre[genre] = [plays[i], (i, plays[i])]
    
    my_val = sorted(list(my_genre.values()), key = lambda x : x[0], reverse = True)
    
    for val in my_val:
        if len(val) < 3:
            answer.append(val[1][0])
        else:
            answer.append(val[1][0])
            answer.append(val[2][0])
    
    return answer
