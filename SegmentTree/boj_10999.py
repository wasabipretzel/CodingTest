# https://www.acmicpc.net/problem/10999

N, M, K = map(int, input().split())

# M : 변경이 일어나는 횟수
# K : 구간의 합을 구하는 횟수
arr = []
tree = [0]*(4*N)
test_cases = []
for _ in range(N):
    num = int(input())
    arr.append(num)

for _ in range(M+K):
    test_list = input().split()
    if len(test_list) == 3:
        a, b, c = map(int, test_list)
        test_cases.append([a, b-1, c-1])
    else:
        a, b, c, d = map(int, test_list)
        test_cases.append([a, b-1, c-1, d]) #b-1 index ~ c-1 index 수에 d를 더한다

def init(arr, tree, node, start, end):
    # leaf node
    if start == end:
        tree[node] = arr[start]
    else:
        init(arr, tree, node*2, start, (start+ end) // 2)
        init(arr, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]
    return

lazy = [0]*(4*N)


# lazy : diff 정보가 저장되어 있음.
# 어떤 값을 바꿔야 할때, l  s  e  r 로 완전히 포함되어 있는 노드는 lazy하게 기록해준다 (실제 tree update x)
# 걸쳐져서 자식 노드를 탐색해야 하는 경우에는 lazy가 아닌 실제로 update해준다.
# pushdown해야 하는 경우
# 1. update시에 기존 lazy에 있던 부분과 겹치면 tree로 기존껀 update해주고(pushdown), 새로 들어온 update를 기록해준다.
# 2. query 들어오는 구간이 lazy의 내용을 포함하면 push down

# 구현
# update_lazy => 특정 노드에 대해 그 노드에 만약 lazy가 기록되어 있으면 tree에 대한 것을 update해주고 자식들에게 lazy propagation (자식들은 update시키지 않음). 이후 현재 노드 lazy 초기화
# update_range -> 구간이 들어왔을 때 start, end 가 만약 완전히 포함된다면 tree의 노드 값을 update해주고 자식 노드들은 tree를 update하지 않고 lazy기록한다

# query ->  구간이 들어왔을 때, update_lazy를 통해 구간에 해당되는 정보를 tree에 update한 후 query정보를 계산한다

def update_lazy(tree, lazy, node, start, end):
    # 만약 lazy 값이 0이 아니라면 (기존의 lazy 가 기록되어 있는 상황)
    if lazy[node] != 0:
        tree[node] += (end - start+1) * lazy[node] # 기존에 밀려있던 lazy값을 tree에 적용시켜줌. 예를 들어 diff가 4라면 node의 구간만큼 곱해줘서 더하면 합이 그만큼 변하는 것
        if start != end:
            # leaf node가 아니라면 자식 노드에게 lazy propagation
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        # tree도 update했고 propagate도 했으니 초기화
        lazy[node] = 0
    return

def update_range(tree, lazy, node, start, end, left, right, diff):
    update_lazy(tree, lazy, node, start, end) # 기존에 밀려있던 lazy 처리하기 -> 해당 노드에 lazy값이 없으면 아무것도 안함. 있으면 새로 밀어내고 update하기 위해 밀어냄
    # 탐색할 필요없는 노드 쳐내기    l  r  s  e  / s  e  l  r
    if right < start or end < left:
        return
    # 구간에 완전히 들어와서 lazy에 기록해줘야 하는 경우  l  s e r
    if left <= start and end <= right:
        tree[node] += (end-start+1)*diff #NOTE 중요!! 가장 상위만 tree update시켜놓고 하위는 lazy만 update해서 값 update안함
        if start != end: #leaf node아닌경우
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return

    # 나머지 구간들의 경우 재귀적으로 탐색
    update_range(tree, lazy, node*2, start, (start+end)//2, left, right, diff)
    update_range(tree, lazy, node*2+1, (start+end)//2+1, end, left, right, diff)
    #하위부터 sum up
    tree[node] = tree[node*2] + tree[node*2+1]
    return


def query(tree, lazy, node, start, end, left, right):
    update_lazy(tree, lazy, node, start, end)
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, lazy, node*2, start, (start+end) // 2, left, right)
    rsum = query(tree, lazy, node*2+1, (start+end) // 2+1, end, left, right)
    return lsum+rsum

init(arr, tree, 1, 0, len(arr)-1)

for each_case in test_cases:
    if each_case[0] == 1:
        update_range(tree, lazy, 1, 0, len(arr)-1, each_case[1], each_case[2], each_case[3])
    else:
        answer = query(tree, lazy, 1, 0, len(arr)-1, each_case[1], each_case[2])
        print(answer)

