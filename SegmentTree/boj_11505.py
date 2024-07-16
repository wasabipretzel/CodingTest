# https://www.acmicpc.net/problem/11505


N, M, K = map(int, input().split())
# M : 수의 변경이 일어나는 횟수
# N : 개수
# K : 구간 합 구하는 횟수

arr = []
tree = [1]*(4*N)

numerator = 1000000007

for _ in range(N):
    num = int(input())
    arr.append(num)


test_cases = []
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        test_cases.append([a, b-1, c]) #1 <= b <= N 번째 이므로 arr index상에서는..0부터 시작해야함
    else:
        test_cases.append([a, b-1, c-1]) # b번째부터 c번째까지 이므로..



#init tree
def init(arr, tree, node, start, end):
    if start == end: #leaf node
        tree[node] = arr[start]
    else:
        init(arr, tree, node*2, start, (start + end) // 2)
        init(arr, tree, node*2+1, (start+end) // 2 +1, end)
        tree[node] = tree[node*2] * tree[node*2+1] % numerator

def query(tree, node, start, end, left, right):
    # 탐색 할 필요 없는 case (벗어난 case) l  r  s  e  or   s  e  l  r
    if right < start or left > end:
        return 1
    # 필요한 node case
    # l s e r
    if left <= start and right>= end:
        return tree[node]
    # 나머지 case에 대해서는 이분탐색
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, node*2+1, (start+end) // 2 +1, end, left, right)
    return lsum*rsum % numerator

def update(arr, tree, node, start, end, index, val):
    # 탐색할 필요 없는 node일경우 제외
    if index < start or index > end:
        return
    # leaf node찾을때까지 내려가서 arr와 tree값 바꿔줌
    if start == end:
        arr[index] = val
        tree[node] = val
        return
    update(arr, tree, node*2, start, (start+end) // 2, index, val)
    update(arr, tree, node*2+1, (start+end) // 2+1, end, index, val)
    tree[node] = tree[node*2] * tree[node*2+1] % numerator

init(arr, tree, 1, 0, len(arr)-1)

for each_case in test_cases:
    a, b, c = each_case
    if a == 1:
        update(arr, tree, 1, 0, len(arr)-1, b, c) # b번째 숫자를 c로 변경
    else:
        answer = query(tree, 1, 0, len(arr)-1, b, c) # b번째 숫자부터 c번째 숫자까지 합
        print(answer % 1000000007)
