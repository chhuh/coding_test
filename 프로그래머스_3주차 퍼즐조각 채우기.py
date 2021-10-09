from collections import deque

def dfs(r, c, board, visited, n):
    
    N = len(board)
    
    block = []
    queue = deque()
    queue.append((r,c))
    
    while queue:
        new_r, new_c = queue.popleft()
        
        if new_r >=0 and new_c>=0 and new_r<N and new_c<N:
            if visited[new_r][new_c] == False and board[new_r][new_c] == n:
                visited[new_r][new_c] = True
                block.append((new_r, new_c))
                queue.append((new_r-1, new_c))
                queue.append((new_r+1, new_c))
                queue.append((new_r, new_c-1))
                queue.append((new_r, new_c+1))
            else:
                continue
        else:
            continue
    return sorted(block)


def solution(game_board, table):
    answer = []
    
    N = len(game_board)
    
    visited_game_board = [[False]*N for _ in range(N)]
    empty_blocks = []
    
    for r in range(N):
        for c in range(N):
            if visited_game_board[r][c] == False and game_board[r][c] == 0:
                empty_blocks.append(dfs(r,c,game_board, visited_game_board, 0))
    
    visited_table = [[False]*N for _ in range(N)]
    blocks1 = []
    
    for r in range(N):
        for c in range(N):
            if visited_table[r][c] == False and table[r][c] == 1:
                blocks1.append(dfs(r,c,table, visited_table, 1))
    blocks = []
    
    for block in blocks1:
        blocks.append(standard_block(block))
    
    def rotate_90(block):
        new = []
        for r, c in block:
            new.append((c, N-1-r))
        return standard_block(sorted(new))
                
    def match(block):
        
        for r in range(N):
            for c in range(N):
                temp = []
                for block_r, block_c in block:
                    new_r = block_r + r
                    new_c = block_c + c
                    
                    if new_r >= 0 and new_r < N and new_c>=0 and new_c<N:
                        temp.append((new_r, new_c))
                if len(temp) == len(block) and temp in empty_blocks:
                    empty_blocks.remove(temp)
                    answer.extend(temp)
                    return True
        return False
    
    for block in blocks:
        for _ in range(4):
            if match(block) == False:
                block = rotate_90(block)
            else:
                break
    
    return len(answer)

def standard_block(block):
    standard_block = []
    
    standard_r = block[0][0]
    standard_c = block[0][1]
    
    for r, c in block:
        standard_block.append((r-standard_r, c-standard_c))
    return sorted(standard_block)
