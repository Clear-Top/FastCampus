import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, w, L = map(int, input().split(' '))
trucks = [i for i in map(int, input().split(' '))]
trucks.reverse()

# 다리길이만큼의 maxlen을 가진 deque 생성
bridge = deque([0] * w, maxlen=w)

# 다리위의 트럭 수
number_of_trucks = 0

# 현재 다리위의 트럭무게 합
weight = 0

# 시간저장
time = 0

weight += trucks[-1]
bridge.append(trucks.pop())
number_of_trucks += 1
time += 1

while weight:
    if trucks:
        if weight + trucks[-1] <= L:
            if number_of_trucks < w:
                number_of_trucks += 1
                time += 1
                weight += trucks[-1]
                bridge.append(trucks.pop())
            else:   # 다리가 꽉차서 못 지나감
                
        else:   # 무게때문에 못 지나감


print(time)