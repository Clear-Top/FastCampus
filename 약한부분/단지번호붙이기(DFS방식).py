# 링크: https://www.acmicpc.net/problem/2667


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

maps = [list(map(int, input().strip())) for _ in range(N)]

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def DFS(cur_p): # cur_p <=> [x,y]
    global cnt
    
    # 지도를 벗어났다면 return False
    if cur_p[0] < 0 or cur_p[0] > N-1 or cur_p[1] < 0 or cur_p[1] > N-1:
        return False
    
    if maps[cur_p[0]][cur_p[1]] == 1:
        maps[cur_p[0]][cur_p[1]] = -1
        cnt += 1
        for vec in zip(dx, dy): # 상, 하, 좌, 우 순서
            next_p = [cur_p[0] + vec[0], cur_p[1] + vec[1]]
            DFS(next_p)
        return True
    return None

result = []
for i in range(N):
    for j in range(N):
        # 시작지점이 '벽'이거나 '이미처리'한 곳이라면 시작조차 X
        cnt = 0
        if DFS([i,j]):   # True 라면 단지가 O, False 는 단지가 X
            result.append(cnt)

print(len(result))
print(*sorted(result), sep = "\n")





