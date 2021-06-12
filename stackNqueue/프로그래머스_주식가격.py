from collections import deque

def solution(prices):
    answer = []
    que_prices = deque(prices)
    while que_prices:
        time = 0
        current_price = que_prices.popleft()
        for i in que_prices:
            time += 1
            if current_price > i:
                break
        answer.append(time)
    return answer
# deque is faster than list
# Deques는 appendleft () 및 popleft ()에 대해 O (1) 속도를 가지며 목록은 insert (0, value) 및 pop (0)에 대해 O (n) 성능을 갖습니다.
