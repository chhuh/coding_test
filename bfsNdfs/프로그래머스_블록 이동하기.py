from collections import deque

def solution(board):
    
    # 코드 간략화를 위한 함수
    def my_append(robot, d):
        if robot not in visited:
            queue.append((robot, d+1))
            visited.add(robot)
    
    N = len(board)
    
    queue = deque()
    queue.append(((0,0,0,1), 0))
    
    visited = set()
    visited.add((0,0,0,1))
    
    while queue:
        robot, d = queue.popleft()
        r1, c1, r2, c2 = robot
        
        # 가로 도착
        if r2 == N-1 and c2 == N-1 and r1 == N-1 and c1 == N-2:
            return d
        
        # 세로 도착
        if r2 == N-1 and c2 == N-1 and r1 == N-2 and c1 == N-1:
            return d
        
        
        
        # 가로인 경우
        if r1 == r2:
            # 오른쪽 이동
            if c2 + 1 < N and board[r2][c2+1] == 0:
                # ㅈ버그
                robot = (r1, c1 + 1, r2, c2+1)
                my_append(robot, d)
            
            # 왼쪽 이동
            if 0 <= c1 - 1 and board[r1][c1-1] == 0:
                robot = (r1, c1-1, r2, c2-1)
                my_append(robot, d)
            
            # 위로 이동( + 회전 : 위 왼, 위 오)
            if r1 - 1 >= 0 and board[r1-1][c1] == 0 and board[r2-1][c2] == 0:
                # 위로 이동
                robot = (r1-1, c1, r2-1, c2)
                my_append(robot, d)
                
                # 위 왼으로 회전
                robot = (r1-1, c1, r1, c1)
                my_append(robot, d)
                
                # 위 오로 회전
                robot = (r2-1, c2, r2, c2)
                my_append(robot, d)
                
            # 아래로 이동( + 회전 : 아 왼, 아 오)
            if r1 + 1 < N and board[r1+1][c1] == 0 and board[r2 + 1][c2] == 0:
                # 아래로 이동
                robot = (r1+1, c1, r2+1, c2)
                my_append(robot, d)
                
                # 아 왼으로 회전
                robot = (r1, c1, r1+1, c1)
                my_append(robot, d)
                
                # 아 오로 회전
                robot = (r2, c2, r2+1, c2)
                my_append(robot, d)
                
        # 세로인 경우
        elif c1 ==c2:
            # 위로 이동
            if r1 - 1 >= 0 and board[r1-1][c1] == 0:
                robot = (r1-1, c1, r1, c1)
                my_append(robot, d)
            # 아래로 이동
            if r2 + 1 < N and board[r2+1][c2] == 0:
                robot = (r2, c2, r2+1, c2)
                my_append(robot, d)
            
            # 오른쪽 이동( + 회전 : 오 위, 오 아)
            if c1 + 1 < N and board[r1][c1+1] == 0 and board[r2][c2+1] == 0:
                # 오른쪽 이동
                robot = (r1, c1+1, r2, c2+1)
                my_append(robot, d)
                
                # 오 위로 회전
                robot = (r1, c1, r1, c1+1)
                my_append(robot, d)
                
                # 오 아로 회전
                robot = (r2, c2, r2, c2+1)
                my_append(robot, d)          
                
            # 왼쪽 이동( + 회전 : 왼 위, 왼 아)
            if c1 - 1 >= 0 and board[r1][c1-1] == 0 and board[r2][c2-1] == 0:
                # 왼쪽으로 이동
                robot = (r1, c1-1, r2, c2-1)
                my_append(robot, d)
            
                # 왼 위로 회전
                robot = (r2, c2-1, r2, c2)
                my_append(robot, d)
                
                # 왼 아로 회전
                robot = (r1, c1-1, r1, c1)
                my_append(robot, d)
                
    return -1
