def checksec(time, time_list):
    cnt = 0
    start = time
    end = time+1000
    for tl in time_list:
        if tl[0] < end and tl[1] >= start:
            cnt += 1
    return cnt

def solution(lines):
    answer = 0
    time_list = []
    start_time = []
    
    for l in lines:
        d, e, t = l.split(' ')
        e = e.split(':')
        t = float(t.replace('s','')) * 1000
        end = (int(e[0])*3600 + int(e[1])*60 + float(e[2])) * 1000
        start = end - t + 1
        time_list.append([start, end])

    for time in time_list:
        answer = max(answer, checksec(time[0], time_list), checksec(time[1], time_list))
        
    return answer
