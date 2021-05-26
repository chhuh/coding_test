def binary(n):
    ans = []
    while n > 0:
        n, r = divmod(n, 2)
        ans.insert(0, r)
    return ans

def solution(s):
    answer = []
    cnt = 0
    zero = 0
    s = list(map(int, s))
    
    while len(s) > 1:
        z = s.count(0)
        zero += z
        s = binary(len(s)-z)
        cnt += 1
        
    print(s)
    answer.append(cnt)
    answer.append(zero)
    return answer
