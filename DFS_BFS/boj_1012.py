# https://www.acmicpc.net/problem/1012

"""
    특정 cell이 1이면 상하좌우에 대해 bfs (연결관계에 대한 정보를 모르니 상하좌우에 대해 수행)
    탐색이 끝난 cell은 0으로 바꿈(방문했다고 하는거임) -> bfs 다 끝나면 연결된 덩어리 탐색이 끝이므로 result += 1
"""
import sys
sys.setrecursionlimit(10**5)


def dfs(i, j):
    if graph[i][j] == 0:
        return False
    else:
        # print(i, j)
        graph[i][j] = 0
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
        return True
    return False

T = int(input())
result_arr = []
for _ in range(T):
    M, N, K = map(int, input().split())
    #M : 열수, N : 행수, K : 배추 개수
    graph = [[0]*(M+2) for _ in range(N+2)] # bfs 할 때 예외조건 안만들고 넉넉하게 하기 위함
    result = 0
    for _ in range(K): #배추 위치
        X, Y = map(int, input().split())
        graph[Y+1][X+1] = 1 # bfs 할 때 예외조건 안만들고 넉넉하게 하기 위함

    for i in range(1, N+2): # bfs 할 때 예외조건 안만들고 넉넉하게 하기 위함
        for j in range(1, M+2): # bfs 할 때 예외조건 안만들고 넉넉하게 하기 위함
            # 이런 문제에서 탐색이란
            # print(i, j)
            flag = dfs(i, j)
            if flag == True:
                result += 1
    result_arr.append(result)

for each_result in result_arr:
    print(each_result)


