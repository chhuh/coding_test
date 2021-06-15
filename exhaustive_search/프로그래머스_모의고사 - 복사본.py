import math
from itertools import permutations

def is_prime_number(x) : 
    if x < 2:
        return False
    
    for i in range(2,int(math.sqrt(x)) + 1) : 
        if x % i == 0 :
            return False
    return True

def solution(numbers):
    answer = []
    number_list = list(numbers)
    for i in range(1, len(number_list) + 1) :
        perlist = list(map(''.join, permutations(number_list, i)))
        for j in list(set(perlist)) :
            if is_prime_number(int(j)) :
                answer.append(int(j))
    answer = len(set(answer))
    return answer
