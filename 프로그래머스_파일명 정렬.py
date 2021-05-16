import re

def solution(files):
    answer = []
    file_list = [re.split('([0-9]+)', i) for i in files]
    file_list.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    answer = [''.join(file) for file in file_list]
    
    return answer
