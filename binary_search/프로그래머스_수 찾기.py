import sys
n1 = sys.stdin.readline()
list1 = sorted(map(int,sys.stdin.readline().split()))
n2 = sys.stdin.readline()
list2 = map(int, sys.stdin.readline().split())

def binary(l, list1, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == list1[m]:
        return 1
    elif l < list1[m]:
        return binary(l, list1, start, m-1)
    else:
        return binary(l, list1, m+1, end)

for l in list2:
    start = 0
    end = len(list1)-1
    print(binary(l,list1,start,end))
