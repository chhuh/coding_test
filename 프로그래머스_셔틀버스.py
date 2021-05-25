def solution(n, t, m, timetable):
    answer = ''
    crew = [int(tt.split(":")[0])*60 + int(tt.split(":")[1]) for tt in timetable]
    bus = [(540 + t*i, 0, None) for i in range(n)]
    crew.sort()
    
    bi, ci = 0, 0
    while ci < len(crew):
        c = crew[ci]
        if bi == len(bus):
            break
            
        if bus[bi][0] >= c and bus[bi][1] < m:
            tt, cnt, _ = bus[bi]
            bus[bi] = (tt, cnt+1, c)
            ci += 1
        else:
            bi += 1
    
    res = bus[-1][0]
    if bus[-1][2]:
        if bus[-1][1] == m:
            print("here")
            res = bus[-1][2] - 1
    
    answer = '%02d:%02d' %(res // 60, res % 60)
        
    return answer
