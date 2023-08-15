import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 회전큐 크기, 찾을 수의 개수
N, M = map(int, input().strip().split(' '))

# 찾을 수
finds = list(map(int, input().strip().split(' ')))

# 회전 큐 초기화
queue = deque([i for i in range(1,N+1)])


mid = int(len(queue) / 2)
number_of_operations = 0

# 찾을 수를 다 pop 할때까지
while finds:
    if queue[0] == finds[0]:
        # print(f'{finds[0]}를 찾았습니다.')
        pop_value = finds.pop(0)
        queue.popleft()
        # mid += 1
        mid = len(queue) // 2
    else:
        # if queue[mid] >= finds[0]:
        if mid >= queue.index(finds[0]):
            while queue[0] != finds[0]:
                queue.append((queue.popleft()))
                number_of_operations += 1
        else:
            while queue[0] != finds[0]:
                queue.appendleft(queue.pop())
                number_of_operations += 1
print(number_of_operations)