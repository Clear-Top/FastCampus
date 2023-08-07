import sys
from collections import deque
from itertools import islice
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().strip())

data = deque(map(int, input().strip().split(' ')))
# print(n, data)

for i in range(n):
    pop_data = data.popleft()
    result_num = -1
    for num in islice(data, 0, len(data), 1):
        # print(f'{pop_data} vs {num}')
        if pop_data < num:
            result_num = num
            break
    print(result_num, end=' ')
