import sys
import copy

dr = [1,-1,0,0]
dc = [0,0,1,-1]

n, m = map(int, sys.stdin.readline().split())

lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_count = 0

def vir():
    global max_count
    copy_lab = copy.deepcopy(lab)
    virus = []
    for r in range(n):
        for c in range(m):
            if copy_lab[r][c] == 2:
                virus.append([r,c])

    while virus:
        v_r, v_c = virus.pop(0)
        for i in range(4):
            new_r, new_c = v_r + dr[i], v_c + dc[i]
            if 0 <= new_r < n and 0 <= new_c < m :
                if copy_lab[new_r][new_c] == 0:
                    copy_lab[new_r][new_c] = 2
                    virus.append([new_r,new_c])
    count = 0
    for l in copy_lab:
        count += l.count(0)
    max_count = max(max_count,count)

def b_t(w):
    if w == 3:
        vir()
        return

    for r in range(n):
        for c in range(m):
            if lab[r][c] == 0:
                lab[r][c] = 1
                b_t(w+1)
                lab[r][c] = 0
                

b_t(0)
print(max_count)
