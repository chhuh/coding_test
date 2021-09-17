import sys

N = int(sys.stdin.readline())

size_list = []
ans = []

for _ in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    size_list.append((weight, height))

for i in size_list:
    temp = 1
    for j in size_list:
        if i[0] < j[0] and i[1] < j[1]:
            temp += 1
    ans.append(temp)
    
print(*ans)
