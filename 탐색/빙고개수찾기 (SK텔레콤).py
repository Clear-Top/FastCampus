import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 5x5 빙고판
bingo_row = 5
bingo_matrix = []
visited = [[False] * 5 for _ in range(5)]
print(visited)

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

result = ()
for r in host_number:
    for c in r:
        # cnt(현재 빙고개수)가 3개면 바로 탈출
        def bingo_init(bingo_matrix, number):
            for r in len(bingo_matrix):
                for c in len(r):
                    if bingo_matrix[r][c] == number:
                        bingo_matrix[r][c] = True
            return (r,c)
        start = bingo_init(bingo_matrix, host_number[r][c])
        
        def bingo_monitor(bingo_matrix):
            for r in range(len(bingo_matrix)):
                print(*r)

        bingo_monitor(bingo_matrix)

        def bingo_hor_check(bingo_matrix, cnt, visited, start):
            '''
            bingo 판을 start 기준으로 수평탐색하여 현재 빙고개수 (cnt) 업데이트

            수평이니까 행은 고정
            '''
            for col in bingo_matrix[start[0]]:
                if col == False:
                    return 0
            return 1

        def bingo_ver_check(bingo_matrix, cnt, visited, start):
            '''
            bingo 판을 start 기준으로 수직탐색하여 현재 빙고개수 (cnt) 업데이트
            '''
            for row in bingo_matrix[start[1]]:
                if row == False:
                    return 0
            return 1

        if bingo_hor_check(bingo_matrix, cnt, visited, start):
            print("수평빙고입니다.")
            cnt+=1
        if bingo_ver_check(bingo_matrix, cnt, visited, start):
            print("수직빙고입니다.")
            cnt+=1

        if cnt == bingo_cnt:
            result.append(r+1, c+1)
            break

print(r * 5 + c)
    
        
    
