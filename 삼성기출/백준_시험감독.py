import sys

N = int(sys.stdin.readline())

room = list(map(int, sys.stdin.readline().split()))

B, C = map(int, sys.stdin.readline().split())

need = 0

for man in room:
    need += 1
    
    if man <= B:
        continue
    else:
        if (man-B)%C == 0:
            need += (man-B)//C
        else:
            need += ((man-B)//C)+1

print(need)
