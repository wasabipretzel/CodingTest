# https://www.acmicpc.net/problem/7576
"""
    여러 곳에서 bfs를 시작해야하는 경우 -> 시작해야 하는 곳을 queue에 넣고 시작
"""
from collections import deque

M, N = map(int, input().split())

graph = [[-1]*(M+2) for _ in range(N+2)]

# 익은 토마토 위치 저장
tomatoes = []

# for i in range(1, N+1):
#     graph[i][1:M+1] = map(int, input().split())

for i in range(1, N+1):
    single_line = input().split()
    for j in range(1, M+1):
        if int(single_line[j-1]) == 1:
            tomatoes.append([i, j])
        graph[i][j] = int(single_line[j-1])

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]


# 토마토가 하나 이상 있는 경우에만 입력으로 주어지기에 토마토 위치를 넣어주고 while 돌리면 됨
result = 0
queue = deque()

# 처음 익은 토마토 위치 다 넣어주기 -> 동시에 그 곳들에서 bfs 시작
for each_tomato in tomatoes:
    queue.append([each_tomato[0], each_tomato[1]])

while queue:
    curr_i, curr_j = queue.popleft()
    for dx, dy in zip(x, y):
        next_i = curr_i + dx
        next_j = curr_j + dy
        if graph[next_i][next_j] == 0:
            queue.append([next_i, next_j])
            graph[next_i][next_j] = graph[curr_i][curr_j] + 1

# 시작부터 모든 토마토가 다 익어있는 상태 -> 0 출력
# 토마토가 절대 모두 익지 못하는 상황 -> -1 => graph 훑으면서 0 있으면 -1 return

# 시작부터 모든 토마토가 다 익어있으면 -1 아니면 1밖에 존재안함 -> max가 1면 0 return


for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == 0:
            print(-1)
            exit()
        else:
            result = max(result, graph[i][j])

if result == 1:
    print(0)
else:
    print(result - 1) #-> 시작을 1로 했기 때문


