from collections import deque

def check(s_list):
    
    stack = []
    for sl in s_list:
        if sl in ('[', '(', '{'):
            stack.append(sl)
        else:
            if not stack:
                return False
            x = stack.pop()
            if sl == ']' and x != '[':
                return False
            elif sl == ')' and x != '(':
                return False
            elif sl == '}' and x != '{':
                return False
    
    if stack:
        return False
    return True

def solution(s):
    answer = 0
    s_list = deque(s)
    for i in range(len(s)):
        s_list.rotate(-1)
        if check(s_list):
            answer += 1
    return answer
