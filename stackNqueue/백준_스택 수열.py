import sys

n = int(sys.stdin.readline().rstrip())

seq = [i for i in range(1, n+1)]
given_seq = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
stack = [seq.pop(0)]
answer = ["+"]

while stack or given_seq:
    if seq == [] and stack[-1] != given_seq[0]:
        answer = ["NO"]
        break
    if stack == [] and seq:
        answer.append("+")
        stack.append(seq.pop(0))
    
    if stack[-1] == given_seq[0]:
        answer.append("-")
        stack.pop()
        given_seq.pop(0)
    
    else :
        answer.append("+")
        stack.append(seq.pop(0))

for ans in answer:
    print(ans + "\n", end ="")
        
