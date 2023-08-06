'우선순위 큐'

import sys
from collections import deque
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

num_test_case = int(input())
results = []
for _ in range(num_test_case):
    N, M = map(int, input().strip().split(' '))
    docs_weight = list(map(int, input().strip().split(' ')))
    docs = deque([i for i in zip(docs_weight, range(0, N))])
    # (weight, doc'th )

    # print(docs)

    cnt = 0
    while docs:
        top = docs[0]
        # print(top, docs[0])
        if top[0] != max(docs, key=lambda x:x[0])[0]:  # 첫 원소의 중요도가 최대가 아니라면
            docs.append(docs.popleft())
        else:
            elem = docs.popleft()
            cnt += 1
            if elem[1] == M:
                print(cnt)
                break

# M 번째 문서가 몇번째로 출력?

    
    