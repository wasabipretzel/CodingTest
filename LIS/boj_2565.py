"""
    LIS (최장 증가 부분 수열) 알고리즘
    -> 원소가 n개인 배열의 일부 원소를 골라내서 만든 부분 수열 중, 각 원소가 이전 원소보다 크다는 ㅈ조건을 만족하고,
    그 길이가 최대인 부분 수열을 최장 증가 부분 수열이라고 한다.

    1. DP적 접근
        => index k를 처음부터 끝까지 돌면서, k 보다 이전 index의 lis마지막 숫자와 비교하면서 만약 k번째 index 값이
        더 크다면, 이전 lis에 붙힐 수 있으므로  update.
        만약 그렇지 않다면 1로 초기화

"""

# https://www.acmicpc.net/problem/2565
# DP적 접근

N = int(input())

graph = []
length = [0 for _ in range(N)]

# [18, 22, 39, 41, 64, 76, 97, 1010] -> LIS 개수 빼고 남은 것이 제외하면 되는 것
# LIS계산방식 arr[i][0], arr[i][-1] 이 있을 때, arr[i-1][0], arr[i-1][-1] 과 비교했을 때 둘다 증가하는 것이어야함

for _ in range(N):
    front, back = map(int, input().split())
    # graph[front] = [front, back]
    graph.append([front, back])

graph.sort()

max_lis = -1
for i in range(0, N):
    length[i] = 1 #초기화 될 경우에도 기본적으로 1이기 때문
    for j in range(0, i):
        # i 이전까지를 비교한다.
        #만약 i index의 front가 i-1 index의 front보다 증가했으며,
        #    i index의 back이 i-1 index의 back보다 증가했으면,
        # update할 수 있는 경우가 됨
        # breakpoint()
        if graph[i][0] > graph[j][0] and graph[i][1] > graph[j][1]:
            length[i] = max(length[i], length[j] + 1) #자신보다 앞의 index의 수열 다음에 올 수 도 있기 때문에 update
            if length[i] > max_lis:
                max_lis = length[i]

print(N - max_lis)


# print(length)
