
# https://www.acmicpc.net/problem/1197
# MST -> 최소간선 -> N-1개의 간선이 될때까지 최소로 정렬한 다음에 연결한다 
# 사이클이 생기지 않도록.. -> 대표 노드가 동일하지 않게끔..


N, M = map(int, input().split())

edge_list = []
parents = [i for i in range(N+1)]

for _ in range(M):
    src, des, cost = map(int, input().split())
    edge_list.append([cost, src, des])

edge_list.sort()


def union(a, b):

    parent_a = find(a)
    parent_b = find(b)

    if parent_a < parent_b:
        parents[parent_b] = parent_a
    else:
        parents[parent_a] = parent_b

    return

def find(a):

    stack = []
    while a != parents[a]:
        stack.append(a)
        a = parents[a]
    
    while stack:
        past_node = stack.pop()
        parents[past_node] = a 
    
    return a

total_edge = 0
index = 0
total_cost = 0
while total_edge != N-1:
    cost, src, des = edge_list[index]
    if src == des:
        index += 1
        continue
    if find(src) != find(des):
        union(src, des)
        total_edge += 1
        total_cost += cost 
    index += 1

print(total_cost)
