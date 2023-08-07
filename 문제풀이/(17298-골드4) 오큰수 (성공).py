import sys
input = sys.stdin.readline

n = int(input().strip())

data = list(map(int, input().strip().split(' ')))
오큰수 = [-1] * n
stack = []

for idx, num in enumerate(data):
    # print(num, idx)
    while stack and stack[-1][0] < num:
        previous = stack.pop()
        오큰수[previous[1]] = num
    stack.append((num, idx))
print(*오큰수)
