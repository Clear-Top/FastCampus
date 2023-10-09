### 2차원 리스트 생성과 접근
def listBreaking():
    print('\n'*2)

# 1. 1차원 리스트 초기화하기 vs 2차원 리스트 초기화하기
size = 10
lst1 = [0] * size   # size 개수만큼의 칸 생성
print(lst1)

row = 20
col = 10
lst2 = [[0]*col for _ in range(row)]  # row * col 크기의 2차원 리스트 생성
print(f'행 개수: {len(lst2)}, 열 개수: {len(lst2[0])}')
for l in lst2: 
    # print(l)
    print(*l)