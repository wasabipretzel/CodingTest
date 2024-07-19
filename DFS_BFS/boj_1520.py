# https://www.acmicpc.net/problem/1520
"""
    -> 그냥 dfs로 풀면 시간초과남.
    -> 왜? 중복 호출이 너무 많이 발생하기 때문. 아래와 같은 경우도 그 예시. 아래 같은 경우가 18 18 사이즈만 되어도 엄청 오래걸림
    3 3
    36 35 34
    35 34 33
    34 33 32
    => 이렇게만해도 이미 중복호출이 너무 많이 발생함
    => bfs + pq로 해결 (DAG이기에 max heap으로 가능)
    visited 가 해당 cell을 경로가 몇 번 지났는지를 update해주는 역할.
    만약 조건에 해당되면서  한번도 지나오지 않았으면 update해주고 pq에 넣어서 경로를 이어나감
    만약 이미 방문했던 적 있으면 중복호출은 하지 말고 대신 지나왔다는 의미로 visited만 update해주고 pq에 넣지 않음.
"""

import heapq

M, N = map(int, input().split())
INF = int(1e9)

graph = [[INF]*(N+2) for _ in range(M+2)]
visited = [[0] * (N+2) for _ in range(M+2)]

for i in range(1, M+1):
    each_line = map(int, input().split())
    graph[i][1:N+1] = each_line

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

# 시작점은 [1,1]
q = []
heapq.heappush(q, ((-1)* graph[1][1], [1, 1])) #max heap
visited[1][1] = 1
# bfs
while q:
    curr_node, curr_loc = heapq.heappop(q)
    curr_i, curr_j = curr_loc

    for dx, dy in zip(x, y):
        next_i = curr_i + dx
        next_j = curr_j + dy
        if graph[curr_i][curr_j] - graph[next_i][next_j] > 0:
            if visited[next_i][next_j] == 0: # 조건에 해당되면서 한번도 방문하지 않은 노드의 경우에 pq에 push => 중복호출을 피하면서 아래 visited값을 update해줌으로써 다른 경로로 오더라도 값을 더해줌
                heapq.heappush(q, ((-1)*graph[next_i][next_j], [next_i, next_j]))
            visited[next_i][next_j] += visited[curr_i][curr_j]

print(visited[M][N])
