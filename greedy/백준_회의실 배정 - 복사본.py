import sys
N = int(sys.stdin.readline())
        
table = []

for _ in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))

table = sorted(table, key = lambda x : x[0])
table = sorted(table, key = lambda x : x[1])

count = 0
last = 0

for i,j in table:
    if i < last:
        continue
    else:
        count += 1
        last = j

print(count)
