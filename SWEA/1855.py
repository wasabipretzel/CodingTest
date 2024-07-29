from collections import deque
T = int(input())

for each_test in range(1, T+1):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    parents = [0 for _ in range(N+1)]
    depth_list = [0 for _ in range(N+1)]
    
    
    queue = deque()
    ancestors = list(map(int, input().split()))
    for idx, parent in enumerate(ancestors):
        graph[idx+2].append(parent)
        graph[parent].append(idx+2)
        parents[idx+2] = parent
    root_node = 1
    initial_depth = 0
    queue.append((root_node, initial_depth))
    prev_node = 0
    answer = 0

    # 두 노드의 공통 조상을 찾을 때 거슬러 올라간 횟수를 서로 합하면 됨
    def LCA(a, b):
        distance = 0
        while depth_list[a] != depth_list[b]:
            if depth_list[a] < depth_list[b]:
                b = parents[b]
                distance+=1
            else:
                a = parents[a]
                distance+=1
        while a != b:
            a = parents[a]
            b = parents[b]
            distance += 2
        return distance

    while queue:
        curr_node, curr_depth = queue.popleft()
        if visited[curr_node] == True:
            continue
        visited[curr_node] = True
        depth_list[curr_node] = curr_depth

        if prev_node == 0 and curr_node == 1:
            answer += 0
        else:
            # 현재 pop된 노드와 이전 노드 간 거리를 계산
            answer += LCA(prev_node, curr_node)

        for each_node in sorted(graph[curr_node]):
            if visited[each_node] == False:
                queue.append((each_node, curr_depth+1))

        prev_node = curr_node

    print(f"#{each_test} {answer}")
