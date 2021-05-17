def changeCode(music_): 
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')    
    return music_ 

def solution(m, musicinfos):
    m = changeCode(m)
    
    candidate = []
    
    for i, music in enumerate(musicinfos):
        info = changeCode(music)
        info = info.split(",")
        length = len(info[-1])
        time = (int(info[1].split(":")[0])*60 + int(info[1].split(":")[1])) - (int(info[0].split(":")[0])*60 + int(info[0].split(":")[1]))
        
        
        if time > length:
            a,b = divmod(time, length)
            melody = a*info[-1] + info[-1][:b]
            
        else:
            melody = info[-1][:time]
            
        if m in melody:
            candidate.append([i, time, info[2]])
    
    if len(candidate) == 0 :
        return "(None)"
    
    else:
        candidate = sorted(candidate, key = lambda x: (-x[1], x[0]))
        return candidate[0][2]
