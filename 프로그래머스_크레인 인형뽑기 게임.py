def solution(board, moves):
    answer = 0
    basket = []
    for m in moves : 
        for b in board:
            if b[m-1] != 0 :
                basket.append(b[m-1])
                if len(basket) > 1:
                    if basket[-2] == basket[-1]:
                        # remove를 쓰면 안되는 이유, 중복되는 값이 있는 경우 앞에 있는것을 먼저 삭제함. 따라서, del 사용
                        del basket[-2]
                        del basket[-1]
                        answer += 2
                b[m-1] = 0
                break
    return answer
