"""
    벨만포드 O(VE)
    -> 음수 가중치 or 전체 그래프에서 음수 사이클의 존재 여부 판단 시 사용

    1. edge list로 그래프 구현 후 최단 경로 list 초기화
        - 최단경로 list 초기화 : 출발 노드 0, 나머지는 무한대로 초기화
        - edge list : [[src, des, cost], ..]
    2. 모든 edge를 N-1번 확인해 정답 리스트 update
        - 사이클이 없을 때, 특정 두 노드의 최단거리를 만들 수 있는 edge 최대 개수는 N-1. (MST가 되는 거지 결국)
        - Update반복횟수가 만약 K번이다 -> 시작점에서 K개의 edge를 사용했을때가 각 노드에 대한 최단거리

        Update조건 : D[s] != inf 이며, D[e] > D[s] + w 일때 D[e] = D[s] + w
                    모든 edge를 돌면서 판단!!
                    -> start node가 무한대가 아니라는건 이미 start node까지 가는 거리가 최단거리로 update된 상태
                    -> D[e] 은 update되지 않은 값 -> D[s] + w : 최단거리 + 경유한 cost 가 더 짧으면 그걸 update
                    -> edge에 음수가 있기 때문에 이완하면서 가는게 아니라 그냥 모든 Edge에 대해 보는 셈

    정답리스트 D[index] -> index 가 사용한 edge 개수
    -> D[index] line에서 값이 무한대가 아니다 -> index개의 edge로 최단거리 갈 수 있는 노드를 말하는 것!!!

    3. 음수 사이클 판별법
    => 특정 두 노드의 최단거리를 만들 수 있는 edge 최대 개수가 N-1보다 클 때..

"""
# https://www.acmicpc.net/problem/11657
from collections import deque

N, M = map(int, input().split())

# graph = [[] for _ in range(N+1)]

# edge_list = [[] for _ in range(N+1)]
edge_list = []

for _ in range(M):
    src, des, cost = map(int, input().split())
    edge_list.append((src, des, cost))
    # edge_list[src].append((des, cost))

INF = int(1e9)
distance_map = [INF for _ in range(N+1)]
distance_map[1] = 0

# 음수 사이클일 경우 -1을 출력

# 최대 N-1개의 edge를 사용하기 때문에 모든 edge를 N-1번 돌면서 최적화
for _ in range(N-1):
    for u, v, w in edge_list:
        if distance_map[u] != INF:
            if distance_map[v] > distance_map[u] + w:
                distance_map[v] = distance_map[u] + w

#-> V-1 동안 그 안에서 E번 돌기에 O(VE)

# 음수 사이클 판별
flag = False
for u, v, w in edge_list:
    if distance_map[u] != INF:
        if distance_map[v] > distance_map[u] + w: #이미 최적값을 update해놨음에도 v를 업데이트 할 수 있는 즉, 거쳤을 때 계속 음수값이 나오는 값이므로 이러면 사이클이 존재
            flag = True

if flag == True:
    print(-1)
else:
    for i in range(2, N+1):
        if distance_map[i] == INF:
            print(-1)
        else:
            print(distance_map[i])




