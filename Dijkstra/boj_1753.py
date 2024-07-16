"""
    heap은 최소 노드를 찾을 때 V -> logN으로 줄여준다

    기존
    1. start node에 대한 처리(visited, 인접 노드 cost update)
    2. 최단경로 경유지 찾기 (V)
    3. 경유지의 인접 노드들마다 돌며 update (V) => 3이 2 안에서 돌기에 O(V^2)
    였다면,

    priority queue O(ElogV)
    1. heapq에 최단거리, node 삽입

"""
import heapq

V, E = map(int, input().split())

start_node = int(input())

INF = int(1e9)
# graph
graph = [[] for _ in range(V+1)]
distance_map = [INF for _ in range(V+1)]

# src, des, weight init
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


q = []

heapq.heappush(q, (0, start_node))
distance_map[start_node] = 0
while q:
    dist, stopover_node = heapq.heappop(q)
    if distance_map[stopover_node] < dist: # 이미 더 짧은 거리를 가지고 있다면 pass -> 여기서 여러 간선인 경우는 이미 pass
        continue
    for each_pair in graph[stopover_node]:
        cost = dist + each_pair[1] #dist : start ~ stopover_node / each_pair[1] : stopover_node ~ each_pair[0] node
        if cost < distance_map[each_pair[0]]:
            distance_map[each_pair[0]] = cost
            heapq.heappush(q, (cost, each_pair[0])) # start ~ each_pair[0] 까지의 비용을 update해서 heap안에 다시 넣음



#start_node부터 i번 정점으로의 최단 경로 값
for i in range(1, V+1):
    if distance_map[i] == INF:
        print("INF")
    else:
        print(distance_map[i])



