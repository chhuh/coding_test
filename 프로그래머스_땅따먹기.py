def solution(land):
    answer = 0
    # DP
    n = len(land)-1
    for i in range(n):
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    answer = max(land[n][0], land[n][1], land[n][2], land[n][3])
    

    return answer
