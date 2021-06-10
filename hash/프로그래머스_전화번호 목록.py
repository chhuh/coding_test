def solution(phone_book):
    answer = True
    phone_book.sort()
    
    hash = {}
    
    for phone in phone_book:
        hash[phone] = 1
    
    for phone in phone_book:
        temp = ""
        for ph in phone:
            temp += ph
            if temp in hash and temp != phone:
                answer = False
                return answer
    
    return answer
