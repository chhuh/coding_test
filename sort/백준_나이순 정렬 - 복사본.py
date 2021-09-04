import sys

n = int(sys.stdin.readline())
member = []


for i in range(n):
    member.append(sys.stdin.readline().split())
    member[i].append(i)

member = sorted(member, key = lambda x : (int(x[0]), x[2]))

for age, name, num in member:
    print("%s %s" %(age, name))
