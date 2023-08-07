import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

n = int(input().strip())

data = list(map(int, input().strip().split(' ')))
오큰수 = [-1] * n
stack = []

for idx, num in enumerate(data):
    # print(num, idx)
    if not stack:
        stack.append((num, idx))    # [0]: 수, [1]: 인덱스
        continue
    # if stack[-1][0] > num: # 작은 수가 들어오면 push (틀림)
    if stack[-1][0] >= num: # 작거나 같은 수가 들어오면 push (수정)
        stack.append((num, idx))
    elif stack[-1][0] < num:
        while stack:
            if stack[-1][0] < num:
                process = stack.pop()
                오큰수[process[1]] = num
                continue
            break
        stack.append((num, idx))
print(*오큰수)
