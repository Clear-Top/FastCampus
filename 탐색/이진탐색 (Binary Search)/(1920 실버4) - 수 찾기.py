import sys
input = sys.stdin.readline

def BinarySearch(data, target):
    if len(data)==0:
        return 0
    else:
        mid = len(data) // 2
        if data[mid] == target:
            return 1
        elif data[mid] > target:
            return BinarySearch(data[:mid], target)
        else: # data[mid] < target
            return BinarySearch(data[mid+1:], target)

# 탐색 당하는 리스트
N = int(input())
A = list(map(int, input().split()))
A.sort()

# 탐색할 숫자들
M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    result = BinarySearch(A, target)
    print(result)