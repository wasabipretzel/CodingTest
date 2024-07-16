
#https://www.acmicpc.net/problem/11779

import heapq
import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

INF = int(1e9)
graph = [[] for _ in range(N+1)]
distance_map = [INF for _ in range(N+1)]
path_map = ["" for _ in range(N+1)]

for _ in range(M):
    src, des, cost = map(int, sys.stdin.readline().split())
    graph[src].append((des, cost))


A, B = map(int, sys.stdin.readline().split())

# A -> B 최소 비용
# 방문 도시 경로 저장.. -> path string으로 해서 붙히자
# distance_map
def dijkstra(start_node, end_node):
    q = []
    minimum_path = ""
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
                path_map[each_node[0]] = path_map[curr_node] + str(curr_node) + " "
                heapq.heappush(q, (cost, each_node[0]))

    return distance_map[end_node]


answer = dijkstra(A, B)
answer_path = path_map[B] + str(B)


print(answer)
print(len(answer_path.split()))
print(answer_path)
