# https://www.acmicpc.net/problem/11404
# 플로이드 워셜

N = int(input())
m = int(input())

INF = int(1e9)
graph = [[] for _ in range(N+1)]
distance_map = [[INF]*(N+2) for _ in range(N+2)]

for _ in range(m):
    src, des, cost = map(int, input().split())
    if distance_map[src][des] == INF:
        distance_map[src][des] = cost
    else:
        distance_map[src][des] = min(distance_map[src][des], cost)

# 자기 자신에 대한 것은 0으로 초기화
for node in range(1, N+1):
    distance_map[node][node] = 0

for k in range(1, N+1): #경유지를 fix한채로 돌면 매 점이 경유지가 바뀔 때마다 거리가  update될 수 있음
    for i in range(1, N+1):
        for j in range(1, N+1):
            distance_map[i][j] = min(distance_map[i][j] , distance_map[i][k] + distance_map[k][j])


for i in range(1, N+1):
    single_line_cost = ""
    for j in range(1, N+1):
        if distance_map[i][j] >= INF:
            single_line_cost += "0 "
        else:
            single_line_cost = single_line_cost + str(distance_map[i][j]) + " "
    print(single_line_cost)



