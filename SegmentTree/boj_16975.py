# https://www.acmicpc.net/problem/16975
"""
    arr의 구간합을 구하는 문제가 아님. 따라서 segment tree는 해당 index범위의 diff값을 가지고 있게끔 한다.
    diff값을 가지고 있다가 만약 새로운 update가 들어오거나 query요청이 들어오면 propagation을 lazy하게 한다.

    Update시
    -> root node부터 내려오면서 만약 노드가 완전히 범위에 포함된다 -> tree[node] += diff 하고 끝
    -> 완전히 포함되지 않는다 -> 자식에게 내 그동안 diff정보를 propagate 해주고 (tree[node*2] += tree[node]) 나를 0으로 초기화한다

    query 시
    -> leaf node까지 탐색하면서 그동안 쌓인 diff값들을 더해줌. 사실 상위에 있는 값들은 0으로 초기화 된 상태이기에 영향이 없음
    -> query함수의 return값은 그동안의 diff값을 한번에 가져오는 것
    
    => arr 초기값에 그동안 diff값을 더해서 print
"""

N = int(input())
tree = [0]*(4*N)
arr = []
test_cases = []

nums = input().split()
for each_num in nums:
    arr.append(int(each_num))
M = int(input())
for _ in range(M):
    test_case = input().split()
    if len(test_case) == 4:
        a, b, c, d = map(int, test_case)
        test_cases.append([a, b-1, c-1, d])
    else:
        a, b = map(int, test_case)
        test_cases.append([a, b-1])


#init 할건없음
def update_range(tree, node, start, end, left, right, diff):
    #범위 밖이면 아무것도 하지 않음    l   r  s  e  /   s  e  l r
    if right < start or end < left:
        return
    #만약 노드가 완전히 포함된다
    if left <= start and end <= right:
        tree[node] += diff
        return
    #자식에게 propagate해주고 자신은 0으로 초기화
    tree[node*2] += tree[node]
    tree[node*2+1] += tree[node]
    tree[node] = 0
    update_range(tree, node*2, start, (start+end) // 2, left, right, diff)
    update_range(tree, node*2+1, (start+end)//2+1, end, left, right, diff)
    return


def query(tree, node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left == start and right == end:
        return tree[node]
    lsum = query(tree, node*2, start, (start+end) // 2, left, right)
    rsum = query(tree, node*2+1, (start+end) // 2+1, end, left, right)
    return lsum+rsum



for each_case in test_cases:
    if each_case[0] == 1:
        update_range(tree, 1, 0, len(arr)-1, each_case[1], each_case[2], each_case[3])
    else:
        update_range(tree, 1, 0, len(arr)-1, each_case[1], each_case[1], 0)
        #leaf node의 번호가 주어졌을 때, segment tree의 index를..
        total_diff = query(tree, 1, 0, len(arr)-1, each_case[1], each_case[1])
        print(arr[each_case[1]] + total_diff)





