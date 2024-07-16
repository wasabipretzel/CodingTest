# https://www.acmicpc.net/problem/2357


N, M = map(int, input().split())

arr = []

for _ in range(N):
    num = int(input())
    arr.append(num)

test_cases = []
for _ in range(M):
    a, b  = map(int,input().split())
    test_cases.append([a-1, b-1]) #번째이므로

tree = [0]* (4*len(arr))  # 1 <= num <= 1억 -> 빈 값을 0으로 하되, 밑에서 min, max할 때 0인 경우 case나눠야함
# 구간합만 기록하는게 아니라 최솟값, 최댓값을 계산해서 list상태로 들고있어야함

def init(arr, tree, node, start, end):
    # start, end가 같은 경우 leaf node
    if start == end:
        tree[node] = [arr[start], arr[start]] #[min, max] of node
    else:
        init(arr, tree, node*2, start, (start+end) // 2)
        init(arr, tree, node*2+1, (start+end) // 2 +1 , end)

        tree[node] = [min(tree[node*2][0], tree[node*2+1][0]), max(tree[node*2][1], tree[node*2+1][1])]
    return


def query(tree, node, start, end, left, right):
    # 더 탐색 안할 경우  l r s e /  s e l r
    if right < start or end < left:
        return [0, 0]
    # node값 자체를 return하고자 하는 경우 l s e r (자식 탐색할 필요없음)
    if left <= start and end <= right:
        return tree[node]
    # 겹치는 경우 -> 이진탐색
    lsum = query(tree, node*2, start, (start+end) // 2, left, right)
    rsum = query(tree, node*2+1, (start+end) // 2 +1, end, left, right)

    # left minimum , right minimum 구하고 만약 있으면 비교
    if lsum[0] == 0 and rsum[0] == 0:
        tot_minimum = 0
    elif lsum[0] == 0 or rsum[0] == 0:
        if lsum[0] == 0:
            tot_minimum = rsum[0]
        else:
            tot_minimum = lsum[0]
    else: #둘다 0이 아님
        tot_minimum = min(lsum[0], rsum[0])

    # left maximum , right maximum 구하고 만약 있으면 비교
    if lsum[1] == 0 and rsum[1] == 0:
        tot_maximum = 0
    elif lsum[1] == 0 or rsum[1] == 0:
        if lsum[1] == 0:
            tot_maximum = rsum[1]
        else:
            tot_maximum = lsum[1]
    else: #둘다 0이 아님
        tot_maximum = max(lsum[1], rsum[1])

    return [tot_minimum, tot_maximum]


init(arr, tree, 1, 0, len(arr)-1)

for each_case in test_cases:
    minimum, maximum = query(tree, 1, 0, len(arr)-1, each_case[0], each_case[1])
    print(minimum, maximum)



