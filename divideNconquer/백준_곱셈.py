import sys

A, B, C = map(int, sys.stdin.readline().split())

def simple(b):
    
    if b==1:
        return A%C
    
    tmp = simple(b//2)
    
    if b%2 == 1:
        return (tmp*tmp*A)%C
    
    if b%2 == 0:
        return (tmp*tmp)%C

print(simple(B))
