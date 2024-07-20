# https://www.acmicpc.net/problem/2211
import heapq


N, M = map(int, input().split())
# 완성되면 MST같은 것이므로 before을 기억
before= [0]*(N+1)

graph = [[] for _ in range(N+1)]
INF = int(1e9)
distance_map = [INF for _ in range(N+1)] 

for _ in range(M):
    src, des, cost = map(int, input().split())
    graph[src].append((des, cost))
    graph[des].append((src, cost))

q = []

heapq.heappush(q, (0, 1)) #cost, start_node
distance_map[1] = 0

while q:
    distance, curr_node = heapq.heappop(q)

    if distance_map[curr_node] < distance:
        continue

    for each_node_info in graph[curr_node]:
        cost = distance + each_node_info[1]

        if cost < distance_map[each_node_info[0]]:
            before[each_node_info[0]] = curr_node
            distance_map[each_node_info[0]] = cost
            heapq.heappush(q, (cost, each_node_info[0]))

# 모든 노드와 연결되어 있으며 최소 -> MST가 됨 이 문제의 경우엔 (모든 dijk이 mst는 아니지만)
print(N-1)
# print(before)
for i in range(2, N+1):
    print(i, before[i])
    

        
