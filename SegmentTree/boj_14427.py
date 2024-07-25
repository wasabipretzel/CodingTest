# 1 i v : A_i를 v로 바꾼다
# 2 : 수열에서 가장 작은 값의 index를 출력. 값이 여러개일때는 index가 작은 것을 출력

# 최소 값 세그먼트 트리를 만들고, 가장 작은 값을 밀어올릴 때 index도 같이 들고다녀야함

# https://www.acmicpc.net/problem/14427

N = int(input())

arr = list(map(int, input().split()))
tree = [0]*(4*N)

M = int(input())

test_cases = []
for _ in range(M):
    single_line = list(map(int,input().split()))
    if len(single_line) == 1:
        test_cases.append([2])
    else:
        a, b, c = single_line
        test_cases.append([a, b-1, c])

def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = [arr[start], start] # value, idx
        return
    init(arr, tree, node*2, start, (start+end)//2)
    init(arr, tree, node*2+1, (start+end)//2+1, end)

    if tree[node*2][0] < tree[node*2+1][0] or tree[node*2][0] == tree[node*2+1][0]:
        tree[node] = [tree[node*2][0], tree[node*2][1]]
    else:
        tree[node] = [tree[node * 2+1][0], tree[node * 2+1][1]]
    return


def update(arr, tree, node, start, end, index, val):

    if end < index or index < start:
        return

    if start == end:
        arr[index] = val
        tree[node] = [val, index]
        return

    update(arr, tree, node*2, start, (start+end)//2, index, val)
    update(arr, tree, node*2+1, (start+end)//2+1, end, index, val)

    if tree[node * 2][0] < tree[node * 2 + 1][0] or tree[node * 2][0] == tree[node * 2 + 1][0]:
        tree[node] = [tree[node * 2][0], tree[node * 2][1]]
    else:
        tree[node] = [tree[node * 2 + 1][0], tree[node * 2 + 1][1]]
    return
#
# def query(tree, node, start, end):
#     return tree[1][1]


init(arr, tree, 1, 0, len(arr)-1)

# print(tree)

for each_case in test_cases:
    if len(each_case) != 1:
        a, b, c = each_case
        update(arr, tree, 1, 0, len(arr)-1, b, c)
    else:
        answer = tree[1][1]+1
        print(answer)
