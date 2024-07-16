
# https://www.acmicpc.net/problem/1916

import heapq
import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# N = int(input()) #도시 (node)
# M = int(input()) #버스 (edge)

INF = int(1e9)
graph = [[] for _ in range(N+1)]
distance_map = [INF for _ in range(N+1)]

for _ in range(M):
    # src, des, cost = map(int, input().split()) # 0 <= cost <= 100,000
    src, des, cost = map(int, sys.stdin.readline().split())
    graph[src].append((des, cost))


# A, B = map(int, input().split())
A, B = map(int, sys.stdin.readline().split())

# A -> B 최소 비용
def dijkstra(start_node, end_node):
    q = []

    heapq.heappush(q, (0, start_node))
    distance_map[start_node] = 0
    while q:
        distance, curr_node = heapq.heappop(q)

        if distance_map[curr_node] < distance: #distance : startnode부터 특정 노드까지 최단 거리라고 계산해서 q에 넣은 것. 근데 이거보다 더 짧다? -> 이미 최적화 완료된 노드라는 뜻
            continue

        for each_node in graph[curr_node]:
            cost = distance + each_node[1]
            if cost < distance_map[each_node[0]]:
                distance_map[each_node[0]] = cost
                heapq.heappush(q, (cost, each_node[0]))

    return distance_map[end_node]


answer = dijkstra(A, B)
print(answer)
