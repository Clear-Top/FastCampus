import sys
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().strip().split(' '))
elements = deque(map(int, input().strip().split(' ')))

left = 0
right = 0
pop = 0
result = 0

elements_copy = copy.deepcopy(elements)

for element in elements_copy:
    if (len(elements) - pop)/2 < element-left+right:
        # top 에 element 가 나올때까지 오른쪽회전
        while elements[-1] != element:
            elements.appendleft(elements.pop())
            right += 1
            result += 1
        elements.pop()
        pop += 1
    else:
        # 첫번째 원소에 element 가 나올때까지 왼쪽회전
        while elements[0] != element:
            elements.append(elements.popleft())
            left += 1
            result += 1
        elements.popleft()
        pop += 1
print(result)