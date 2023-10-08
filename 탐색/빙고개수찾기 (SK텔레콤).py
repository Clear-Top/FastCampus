import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 5x5 빙고판
bingo_row = 5
bingo_matrix = []
visited = [[0] * 5 for _ in range(5)]

# 빙고판 초기화
for _ in range(bingo_row):
    bingo_matrix.append([val for val in map(int, input().split())])

# 사회자가 수를 부를때마다 빙고개수를 파악해야 함
bingo_cnt = 3
cnt = 0

# 사회자가 부르는 수
host_number = []
for _ in range(5):
    host_number.append([val for val in map(int, input().split())])

result = []
skip_hor = False
skip_ver = False
for r in range(5):
    def bingo_hor_check(visited, start):
            '''
            bingo 판을 start 기준으로 수평탐색하여 현재 빙고개수 (cnt) 업데이트
            '''
            for col in visited[start[0]]:
                if col == 0:
                    return 0
            return 1
    if not skip_hor:
        if bingo_hor_check(visited, start):
                bingo_monitor(visited)
                print(f"{r} 에서 수평빙고입니다.")
                cnt+=1
                skip_hor = True
    for c in range(5):
        # cnt(현재 빙고개수)가 3개면 바로 탈출
        def bingo_init(bingo_matrix, visited, number):
            '''
            사회자가 부른 숫자에 해당하는 위치를 방문처리
            '''
            for r in range(5):
                for c in range(5):
                    if bingo_matrix[r][c] == number:
                        visited[r][c] = 1
                        return (r,c)
            return None
    
        start = bingo_init(bingo_matrix, visited, host_number[r][c])
        
        # 빙고판 모니터링
        def bingo_monitor(visited):
            for r in range(5):
                for c in range(5):
                    print("{0:>3}".format(bool(visited[r][c])), end=' ')
                print()
        # bingo_monitor(visited)

        def bingo_ver_check(visited, start):
            '''
            bingo 판을 start 기준으로 수직탐색하여 현재 빙고개수 (cnt) 업데이트
            '''
            for row in visited[start[1]]:
                if row == 0:
                    return 0
            return 1

        if bingo_ver_check(visited, start):
            bingo_monitor(visited)
            print(f"({r}, {c}) 기준으로 수직빙고입니다.")
            cnt+=1

        if cnt == bingo_cnt:
            result.append(r+1)
            result.append(c+1)
            break
    skip_hor = False
    skip_col = False

print(result[0] * 5 + result[1])
    
        
    
