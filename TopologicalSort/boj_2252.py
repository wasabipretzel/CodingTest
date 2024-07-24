# https://www.acmicpc.net/problem/2252

"""
    위상정렬 O(V+E)
    -> DAG 그래프에 대해 방향성을 거스르지 않도록 순서대로 나열

    Queue / Stack 둘다 구현가능
    Queue
    1. indegree가 0인 모든 노드들을 queue에 넣기
    2. q에서 하나씩 빼서 노드에서 나가는 간선을 그래프에서 제거 -> 새롭게 indegree가 0인 노드들을 queue에 넣는다
    3. q에 들어가는 순서가 위상정렬 순서

    => 사이클 판별 : q가 모든 노드를 방문하기 전에 끝나면 사이클 존재 -> 사이클의 어떤 원소도 q에 들어가지 않는다
"""

from collections import deque

N, M = map(int, input().split())
# N : 학생 수, M : 키를 비교한 회수
graph = [[] for _ in range(N+1)] # 학생 번호가 1 ~ N

#indegree도 알고있어야함
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split()) #A ->B
    graph[A].append(B)
    indegree[B] += 1

q = deque()

for node_num in range(1, N+1):
    if indegree[node_num] == 0:
        q.append(node_num)
result = []
while q:
    curr_node = q.pop()
    # curr_node와 연결된 노드들에 대해 그 노드의 indegree를 -1 => 만약 0이면 queue에 추가
    result.append(curr_node)

    for adjacent_node in graph[curr_node]:
        indegree[adjacent_node] -= 1
        if indegree[adjacent_node] == 0:
            q.append(adjacent_node)

print(*result)
