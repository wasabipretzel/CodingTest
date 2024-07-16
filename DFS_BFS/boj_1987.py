#https://www.acmicpc.net/problem/1987

"""
    널찍히 잡아놓고 종료조건을 중복 알파벳 or cell value 값이 0이거나
"""

R, C = map(int, input().split())

graph = [[0]*(C+2) for _ in range(R+2)]

for i in range(1, R+1):
    linevalue = input()
    for j in range(1, C+1):
        graph[i][j] = linevalue[j-1]


length_history = [] #말이 dfs할때마다 길이 기록 -> 나중에 max값으로 답 print


# 필요한 것들 init
# dfs시에 stack에는 [i, j, current length, before node cache list] 이렇게 가지고 다녀야함
curr_length = 1
stack = []

dx = [0, 0, -1, +1]
dy = [1, -1, 0, 0]

# 특정 cell에 대해 적합한지 test
def check_feasible(x, y):
    """
        node_cache에 후보군 값이 없으며, visited되지 않았으며, 후보군 값이 0이 아니어야 함
    :return:
    """
    candidate_node = graph[x][y]
    if candidate_node != 0 and candidate_node not in path:
        return True
    else:
        return False

# start node
stack.append([1, 1, curr_length, ""])

#dfs start
while stack:
    curr_node_info = stack.pop()
    i, j, curr_length, path = curr_node_info[0], curr_node_info[1], curr_node_info[2], curr_node_info[3]
    curr_node_value = graph[i][j]
    # node_cache.append(curr_node_value) #이미 stack에 들어있는 경우는 탐색가능한 경우만 들어있으므로..
    path += curr_node_value

    #상하좌우 test
    check_end_flag = 0
    for delta_x, delta_y in zip(dx, dy):
        x = i + delta_x
        y = j + delta_y
        if check_feasible(x, y):
            # append
            stack.append((x, y, curr_length+1, path)) #NOTE  immutable인 str로 해야함. 아니면 처음부터 tuple쓰던가..
        else:
            check_end_flag += 1
    if check_end_flag == 4: #네 방향 다 불가 (즉 현재가 leaf node)
        length_history.append(curr_length) #max value랑 비교해서 더 크면  update하도록 한다... 이게 아니면 max 에서 전부 다 비교해야함 똑같은가..?

print(max(length_history))













