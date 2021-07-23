import sys

n = int(sys.stdin.readline().rstrip())

stack = []

for i in range(n):
    input = sys.stdin.readline().rstrip()
    
    input_list = input.split()
    
    if input_list[0] == "push":
        stack.append(input.split()[1])
        
    if input_list[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
        
    if input_list[0] == "size":
        print(len(stack))
        
    if input_list[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
        
    if input_list[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
