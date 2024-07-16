# https://www.acmicpc.net/problem/1922

"""
    MST Kruskal

    1. Edge list를 오름차순으로 정렬
    2. edge를 돌면서 연결했을 때, cycle이 생기면(find 연산으로 탐색) 연결하지 않고 안생기면 연결(Union 연산)
    3. 2번을 연결된 edge가 n-1개가 될 때까지 수행
"""

N = int(input()) #node
M = int(input()) #total edge

edge_list = []
parents = [i for i in range(N+1)] #자기 자신을 부모로 하게끔 초기화

for _ in range(M):
    src, des, cost = map(int, input().split())
    edge_list.append((cost, src, des))

edge_list.sort() #오름차순 정렬


#Union find
def union(a, b):
    # 부모 노드 찾아서 잇기
    parent_a = find(a)
    parent_b = find(b)

    if parent_a < parent_b:
        parents[parent_b] = parent_a
    else:
        parents[parent_a] = parent_b
    return


def find(a):
    # 부모 노드 찾기
    # index와 value가 같게 하기
    stack = []
    while parents[a] != a:
        stack.append(a)
        a = parents[a]

    #부모노드는 찾음. 이전 노드들의 부모 update
    while stack:
        past_node = stack.pop()
        parents[past_node] = a

    return a


cnt = 0
index = 0
total_cost = 0
edges = []
while cnt != N-1:
    cost, src, des =edge_list[index]
    # 연결했을 때 사이클이 생기면(src와 des의 부모가 같으면) 연결하지 않는다.
    find_src = find(src)
    find_des = find(des)
    if find(src) != find(des):
        union(src, des)
        cnt += 1
        total_cost += cost
        edges.append((src, des))
        # print(src, des)
        # print(find_src, find_des)
        # print(parents)
        # print("======================")
    index += 1

print(total_cost)
# print(edges)






