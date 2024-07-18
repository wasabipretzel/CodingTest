# https://www.acmicpc.net/problem/1260

from collections import deque


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    src, des = map(int, input().split())
    graph[src].append(des)
    graph[des].append(src)



# dfs
stack = []
stack.append(V)

dfs_result = ""
while stack:
    curr_node = stack.pop()
    if visited[curr_node] == True:
        continue
    else:
        visited[curr_node] = True
        dfs_result = dfs_result + str(curr_node) + " "

    for each_node in sorted(graph[curr_node], reverse=True): #큰 것이 먼저 나오도록 
        if visited[each_node] == False:
            stack.append(each_node)
    

bfs_result = ""
queue = deque()
queue.append(V)
visited = [False for _ in range(N+1)]

while queue:
    curr_node = queue.popleft()
    if visited[curr_node] == True:
        continue
    else:
        visited[curr_node] = True
        bfs_result = bfs_result + str(curr_node) + " "

    for each_node in sorted(graph[curr_node]):
        if visited[each_node] == False:
            queue.append(each_node)


print(dfs_result)
print(bfs_result)
