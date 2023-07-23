# %%imteit: 프로그램 수행시간 측정
from memory_profiler import profile
import random
import time

@profile
def BinarySearch(data, target):
    if len(data)==0:
        return False, None
    else:
        mid = len(data) // 2
        if data[mid] == target:
            return (True, mid)
        elif data[mid] > target:
            return BinarySearch(data[:mid], target)
        else: # data[mid] < target
            return BinarySearch(data[mid+1:], target)

# data = random.sample(range(10000000), 1000000)
# target = random.randint(1,10000000)
data = random.sample(range(10000000), 1000000)
target = random.randint(1,10000000)

data.sort()
# print('정렬된 집합' + str(data) + '입니다.')
# print(f'target={target}')

start = time.time()
index, result = BinarySearch(data,target)
end = time.time()
print(f'프로그램 총 시간: {end-start: .4f} sec')

if result:
    print(f"{target}이 존재하며, {index}번째 index에 위치합니다.")
else:
    print(f"{target}이 존재하지 않습니다.")