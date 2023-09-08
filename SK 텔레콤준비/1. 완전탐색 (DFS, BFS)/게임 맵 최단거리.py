'''
maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.

처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

maps	                                                        answer
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	11
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	-1

'''

import sys
import copy
input = sys.stdin.readline



# dest[0]: 세로, dest[1]: 가로
def DFS(maps, posit, dest, vecs, visited, cnt):
    if posit[0] == dest[0] and posit[1] == dest[1]:
        if cnt < answer:
            answer = cnt
        return
    
    for vec in vecs:
        # vec[0]: 가로, vec[1]: 세로
        if posit[0] + vec[0] >= dest[1] or posit[1] + vec[1] >= dest[0]:
            continue
        elif posit[0] + vec[0] < dest[1] or posit[1] + vec[1] < dest[0]:

    return


def solution(maps):
    global answer

    visited = copy.deepcopy(maps) 

    answer = 0

    # 동 서 남 북
    vec = [(1,0),(-1,0),(0.-1),(0,1)]
    current_posit = (0,0)

    DFS(maps, current_posit, (len(maps), len(maps[0])), vec, visited, 0)
    print(len(maps), len(maps[0]))
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
#print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))