def solution(places):
    answer = []
    
    for place in places:
        for i, p in enumerate(place):
            place[i] = "X" + p + "X"
        place.insert(0, "X"*len(place[0]))
        place.append("X"*len(place[0]))
        
        my_flag = 1
        
        for i in range(1, len(place) - 1):
            for j in range(1, len(place[0]) - 1):
                if place[i][j] == "P":
                    if place[i+1][j] == "P" or place[i][j+1] == "P" or place[i-1][j] == "P" or place[i][j-1] == "P":
                        my_flag = 0
                    if place[i-1][j+1] == "P":
                        if place[i-1][j] == "O" or place[i][j+1] == "O":
                            my_flag = 0
                    if place[i-1][j-1] == "P":
                        if place[i-1][j] == "O" or place[i][j-1] == "O":
                            my_flag = 0
                    if place[i+1][j+1] == "P":
                        if place[i+1][j] == "O" or place[i][j+1] == "O":
                            my_flag = 0
                    if place[i+1][j-1] == "P":
                        if place[i+1][j] == "O" or place[i][j-1] == "O":
                            my_flag = 0
                            
                    if place[i-1][j] == "O":
                        if place[i-2][j] == "P":
                            my_flag = 0
                    if place[i+1][j] == "O":
                        if place[i+2][j] == "P":
                            my_flag = 0
                    if place[i][j-1] == "O":
                        if place[i][j-2] == "P":
                            my_flag = 0
                    if place[i][j+1] == "O":
                        if place[i][j+2] == "P":
                            my_flag = 0
        answer.append(my_flag)

    return answer
