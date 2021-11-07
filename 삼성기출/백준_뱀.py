import sys
import copy

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

apple = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(K)]

L = int(sys.stdin.readline())

temp_arrows = [list(sys.stdin.readline().split()) for _ in range(L)]

arrows = dict()

for arrow in temp_arrows:
    arrows[int(arrow[0])] = arrow[1]

time = 0

my_arrow = 0

snake = [[1,1]]

dr = [0,1,0,-1]
dc = [1,0,-1,0]



while True:
    temp = copy.deepcopy(snake[-1])
    temp = [temp[0]+dr[my_arrow], temp[1] + dc[my_arrow]]

    time += 1

    # 종료조건
    if temp in snake:
        print(time)
        break

    elif temp[0] > N or temp[1] > N or temp[0] < 1 or temp[1] < 1:
        print(time)
        break

    # 종료가 아닌경우
    snake.append(temp)
    
    if snake[-1] in apple:
        apple.remove(snake[-1])
    else:
        snake.pop(0)

    # 방향전환
    if time in arrows.keys():
        if arrows[time] == "D":
            if my_arrow == 3:
                my_arrow = 0
            else:
                my_arrow += 1
        else:
            if my_arrow == 0:
                my_arrow = 3
            else:
                my_arrow -= 1

