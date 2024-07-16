# https://www.acmicpc.net/problem/1504
"""
    1 -> N 사이에 V1 / V2를 무조건 경유해야함
    두 가지를 비교하면됨
    (1) 1 -> v1 -> v2 -> N
    (2) 1 -> v2 -> v1 -> N
    => 만약 1 -> v1 사이에 v2를 이미 경유한다면 (1)이 아닌 (2)가 더 짧을 것이다.
    따라서 1 -> N dijkstra 한번, v1, v2를 시작으로 하는 dijkstra 총 3번을 수행해서 (1), (2)를 얻은 다음 min을 찾으면 됨
"""

import heapq


INF = int(1e9)
N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w)) #무방향 그래프

V1, V2 = map(int, input().split())

def dijkstra(start_node):
    distance_map = [INF for _ in range(N + 1)]
    q = []

    #heap start node 추가
    distance_map[start_node] = 0
    heapq.heappush(q, (0, start_node))

    while q:
        #distance : 연결된 최단 노드 뽑기
        distance, curr_node = heapq.heappop(q)

        if distance_map[curr_node] < distance: #이미 지나온 경우(최단거리 만든 노드의 경우) pass
            continue

        for each_pair in graph[curr_node]:
            #경유 비용
            # 1 -> each_pair[0] 까지 거리
            cost = distance + each_pair[1] #curr_node -> target node거리
            if cost < distance_map[each_pair[0]]:
                distance_map[each_pair[0]] = cost
                heapq.heappush(q, (cost, each_pair[0]))
    return distance_map


# 1 -> N
origin_distance = dijkstra(1)
v1_start = dijkstra(V1) #V1 -> N
v2_start = dijkstra(V2) #V2 -> N

# 1 -> V1 -> V2 -> N
distance_1 = origin_distance[V1] + v1_start[V2] + v2_start[N]
# 1 - > V2 -> V1 -> N
distance_2 = origin_distance[V2] + v2_start[V1] + v1_start[N]


result = min(distance_1, distance_2)

if result < INF:
    print(result)
else:
    print(-1)




