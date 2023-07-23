''' 프림알고리즘 특징
1. 최소신장 트리 알고리즘
2. 간선정보가 많을 때 사용
3. 선택된 정점과 연결된 모든 간선들 중에서 가중치가 가장작은 간선을 선택함
4. Heap 자료구조를 사용
'''

''' 프림알고리즘 과정
1. 정점 선택
2. 선택된 정점에 연결된 간선들 중에서 가중치가 가장 작은 것 선택
3. 싸이클이 없을때 연결
4. 1-3 반복 until 모든 정점이 선택될 때까지
'''

''' heap 복습
1. Import 하기
    - import heapq
    - from heapq import heappush, heappop

2. Heappush 하기
    - heapq.heappush(heap, data)

3. Heappop 하기
    - heapq.heappop(heap)

4. Heapify 하기
    - heapq.heapify(data)

5. N 번째 큰/작은 수 찾기 (nlargest, nsmallest)
    - heapq.nlargest(N, heap)
    - heaq.nsmallest(N, heap)
'''
import sys
from collections import defaultdict
from heapq import heappush, heappop, heapify

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

nodes, edges = map(int, input().split())
mygraph = defaultdict(list) # 빈 그래프 (딕셔너리로)

print(f'노드개수: {nodes}, 엣지개수: {edges}')

for i in range(edges):
    # input style: v1, v2, weight
    v1, v2, weight = map(int, input().split())

    # 무방향그래프이므로 양쪽 정점에 간선 정보추가
    # (weight, start, end)
    mygraph[v1].append((weight, v1, v2))
    mygraph[v2].append((weight, v2, v1))
    print('입력완료'+f'현재 {i+1}개 입력완료')

def prim(start_node, mygraph):
    print('프림알고리즘 수행 중...')
    mst = []            # 최소신장트리의 간선들
    visited_nodes = [False] * (nodes+1)  # 최소신장트리의 노드들
    adjacent_edges = mygraph[start_node] # 지금까지 선택된 정점들과 인접한 간선들 (리스트)

    heapify(adjacent_edges) # 힙으로 변환
    visited_nodes[start_node] = True

    while adjacent_edges:
        weight, start, end = heappop(adjacent_edges)
        if visited_nodes[end] == False:
            visited_nodes[end] = True
            mst.append((weight, start, end))
            for edge in mygraph[end]:
                if visited_nodes[edge[2]] == True:
                    continue    # 싸이클방지
                heappush(adjacent_edges, edge)

    return mst, visited_nodes

mst, visited_nodes = prim(1, mygraph)

if all(visited_nodes[1:]):
    print("MST 입니다")
else:
    print("MST가 아닙니다.")
print(mst)


''' 입력예시용
7 11
1 2 7
1 4 5
2 3 8
2 4 9
4 6 6
3 5 5
4 5 7
6 5 8
2 5 7
6 7 11
5 7 9
'''