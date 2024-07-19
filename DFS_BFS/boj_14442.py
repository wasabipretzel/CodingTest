# https://www.acmicpc.net/problem/14442
"""
    3차원 배열로 visited를 만들어서
    [x][y][0] -> 벽 안부수고 온 경우의 최단거리
    [x][y][1] -> 벽 부수고 온 경우의 최단거리
    를 기록
"""

from collections import deque

N, M, K = map(int, input().split())

graph = []
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
# [x][y][0] : -> 벽 안부순 경로에 대한 거리
# [x][y][k] : -> 벽 k개 부순 경로에 대한 거리

for _ in range(N):
    single_line = list(map(int, input()))
    graph.append(single_line)

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

queue = deque()
# x, y, flag
# flag가 1이면 벽 부순 놈
queue.append((0, 0, 0))

while queue:
    curr_i, curr_j, flag = queue.popleft()

    if curr_i == N-1 and curr_j == M-1:
        print(visited[curr_i][curr_j][flag])
        exit()

    for dx, dy in zip(x, y):
        next_i = curr_i + dx
        next_j = curr_j + dy

        if next_i < 0 or next_i >= N or next_j < 0 or next_j >= M:
            continue

        if graph[next_i][next_j] == 1 and flag < K and visited[next_i][next_j][flag+1] == 0:
            visited[next_i][next_j][flag+1] = visited[curr_i][curr_j][flag] + 1
            queue.append((next_i, next_j, flag+1))
        elif graph[next_i][next_j] == 0 and visited[next_i][next_j][flag] == 0:
            visited[next_i][next_j][flag] = visited[curr_i][curr_j][flag] + 1
            queue.append((next_i, next_j, flag))



print(-1)

