import sys

input = sys.stdin.readline

lsts = [list(map(int, input().split(' '))) for _ in range(5)]

max = [0,0] # (idx, score)

for idx, lst in enumerate(lsts):
    if max[1] < sum(lst):
        max[0] = idx
        max[1] = sum(lst)
print(max[0]+1, max[1])

# 4분 30초
# 시간: 40 ms
# 공간: 31256 KB