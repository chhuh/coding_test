def solution(genres, plays):
    answer = []
    genre_play_sum = {}
    genre_dic ={}
    
    for i in range(len(genres)):
        if genres[i] not in genre_dic.keys():
            genre_dic[genres[i]] = [(plays[i], i)]
            genre_play_sum[genres[i]] = plays[i]
        else:
            genre_dic[genres[i]].append((plays[i], i))
            genre_play_sum[genres[i]] = genre_play_sum[genres[i]]+ plays[i]
            
    sorted_play_sum = sorted(genre_play_sum.items(), key=lambda x: x[1], reverse = True)   
    
    for key in sorted_play_sum:
        sorted_list = genre_dic[key[0]]
        sorted_list = sorted(sorted_list, key = lambda x : (-x[0], x[1]))
        
        for i in range(len(sorted_list)):
            if i == 2:
                break
            answer.append(sorted_list[i][1])
    return answer
