# https://www.acmicpc.net/problem/11437

"""
    Tree를 class로 안짜는 것이 나은 이유 : 이진트리가 아닐 경우 확장하기 어려움
    => 그냥 adjacency list가 짱
"""



N = int(input())

graph = [[] for _ in range(N+1)] # root 가 1이니까
parents = [0 for _ in range(N+1)] # index node의 부모가 어떤 노드인지

# 해당 노드의 depth가 몇인지
depth_list = [0] * (N+1) #root가 1이니까
visited = [False] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


M = int(input()) #test case num
test_case = []
#graph도 만들고 depth도 찾았으니 LCA 받을 준비 완료
for _ in range(M):
    A, B = map(int, input().split())
    test_case.append([A, B])




# 트리를 dfs 순회하면서 노드 별 depth, 부모 노드를 찾는다
root_node = 1
depth = 0
stack = []
stack.append([root_node, depth])

while stack:
    curr_node, curr_depth = stack.pop()
    if visited[curr_node]:
        continue
    visited[curr_node] = True
    depth_list[curr_node] = curr_depth

    for each_node in graph[curr_node]:
        if visited[each_node] == False: #연결된 노드 중 방문하지 않은 노드에 대해 부모를 설정 후 depth 추가
            parents[each_node] = curr_node
            stack.append([each_node, curr_depth+1])


#LCA
def LCA(a, b):
    # 깊이가 동일해지도록 조정
    while depth_list[a] != depth_list[b]:
        if depth_list[a] < depth_list[b]:
            b = parents[b]
        else:
            a = parents[a]

    # 노드가 같아지도록
    while a != b:
        a = parents[a]
        b = parents[b]
    return a


for each_case in test_case:
    print(LCA(each_case[0], each_case[1]))



