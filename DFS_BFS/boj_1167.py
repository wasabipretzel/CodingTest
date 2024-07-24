# https://www.acmicpc.net/problem/1167
"""
    구하려는 것 : 두 점 사이의 거리 중 가장 긴 것
    핵심
    -> 임의의 노드에서 가장 멀리 있는 노드는 지름의 양 끝점 중 하나이다.

    => 따라서 어떤 노드로부터 가장 먼 노드 V1을 구함
    => V1 노드로부터 dfs을 해서 가장 먼 노드 V2를 구하면 
    V1-> V2가 지름임
"""

import heapq

V = int(input())

tree = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

for _ in range(V):
    single_line = input().split()
    start_node = int(single_line[0])
    for idx in range(1, len(single_line)-1, 2):
        tree[start_node].append([int(single_line[idx]), int(single_line[idx+1])]) #  tree[src] -> [des, cost], [des, cost]...


stack = [] # [node와 depth정보를 추가] -> 갈 곳이 없으면 leaf node
# root node를 1로 설정해서 1과 관련된 node들 추가
for adjacent_node in tree[1]:
    stack.append((adjacent_node[0], adjacent_node[1]))
visited[1] = True

# 특정 노드 기준 자식 노드들이 2개 이상 -> 자식 노드들 끼리 가장 큰 것 2개 합 과 누적 + 자식의 합  -> 가장 큰 것 2개 합이 더 크면 heap에 추가
# 자식 중 가장 큰 것 두개 합  -> heap에 넣고 leaf node heap 에 넣으면 될3듯?

first_max_dist = -1
first_max_node = -1
while stack:
    curr_node, curr_cost = stack.pop()
    if visited[curr_node] == True:
        continue
    visited[curr_node] = True
    if first_max_dist < curr_cost:
        first_max_dist = curr_cost
        first_max_node = curr_node

    # curr node의 adjacent node중 방문하지 않은 노드(자식들)를 찾는다
    for adjacent_node_info in tree[curr_node]:
        next_node, next_cost = adjacent_node_info[0], adjacent_node_info[1] #curr_node와 next_cost를 연결
        if visited[next_node] == False:
            stack.append([next_node, curr_cost + next_cost])

# print(first_max_node, first_max_dist)

# 한번더 dfs
final_max_dist = -1
final_max_node = -1
visited = [False for _ in range(V+1)]

stack = [] # [node와 depth정보를 추가] -> 갈 곳이 없으면 leaf node
# root node를 1로 설정해서 1과 관련된 node들 추가
for adjacent_node in tree[first_max_node]:
    stack.append((adjacent_node[0], adjacent_node[1]))

# 특정 노드 기준 자식 노드들이 2개 이상 -> 자식 노드들 끼리 가장 큰 것 2개 합 과 누적 + 자식의 합  -> 가장 큰 것 2개 합이 더 크면 heap에 추가
# 자식 중 가장 큰 것 두개 합  -> heap에 넣고 leaf node heap 에 넣으면 될3듯?
visited[first_max_node] = True
while stack:
    curr_node, curr_cost = stack.pop()
    if visited[curr_node] == True:
        continue
    visited[curr_node] = True
    if final_max_dist < curr_cost:
        final_max_dist = curr_cost
        final_max_node = curr_node

    # curr node의 adjacent node중 방문하지 않은 노드(자식들)를 찾는다
    for adjacent_node_info in tree[curr_node]:
        next_node, next_cost = adjacent_node_info[0], adjacent_node_info[1] #curr_node와 next_cost를 연결
        if visited[next_node] == False:
            stack.append([next_node, curr_cost + next_cost])


print(final_max_dist)


