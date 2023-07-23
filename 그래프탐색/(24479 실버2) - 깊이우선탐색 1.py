''' 문제 설명
N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

< 의사코드 >
dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}
'''

''' 입출력 설명
첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.

다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다. (1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. i번째 줄에는 정점 i의 방문 순서를 출력한다. 시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.
'''

''' 입출력 예시
5 5 1
1 4
1 2
2 3
2 4
3 4

1
2
3
4
0
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 입력 (노드개수, 간선개수, 시작노드)
N, M, R = map(int, input().split())

# 초기화 (그래프는 인접리스트로)
# 첫번째 공간은 비워두는 걸로
graph = [[] for _ in range(N+1)]
visited_node = [False] * (N+1)
start_node = R
results = [0] * (N+1)
order_index = 1

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 각 인접리스트들을 오름차순 정렬
for nodes in graph:
    nodes.sort()

stack = [start_node]

def DFS(graph, stack):
    global order_index
    removed_node = stack.pop()
    visited_node[removed_node] = True
    results[removed_node] = order_index
    order_index += 1

    for node in graph[removed_node]:
        if visited_node[node] == False:
            stack.append(node)
            DFS(graph, stack)

DFS(graph, stack)

for index in range(1, len(results)):
    print(results[index])

# 결과
# Runtime = 0.6 sec, Memory Usage = 71 MB 