# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 0은 벽, 1이 가능한 길
# BFS (DFS는 일반적으로 모든 경로를 전부 탐색해야하기 때문에 효율성이 떨어짐)

from collections import deque

def BFS(maps, Q):
    global max_row, max_col
    global dx, dy

    Q.append((0,0))
    
    while Q:
        x, y = Q.lefpop()
        
        if x == max_col-1 or y == max_row-1:    # 끝에 도달했다면
            return 1
        for move in zip(dy,dx): # 가로, 세로 이동
            next = ()
            next.append(x+move[0])
            next.append(y+move[1])

            # 지도를 벗어났을때

            # 벽에 마주쳤을 때

            # 이미 방문했을 때


    
    pass

def solution(maps):  
    Q = deque()
    max_row = len(maps)
    max_col = len(maps[0])
    # 이동순서: 동  서  남  북
    dx = [0, 0, 1, -1]
    dy = [1, -1 ,0 ,0]

    BFS(maps, Q)
    
    return 

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))