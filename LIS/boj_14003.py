# https://www.acmicpc.net/problem/14003

N = int(input())

arr = list(map(int, input().split()))

lis_length = [] # lis 후보군 숫자 및 arr에서의 index를 저장 (숫자가 같은 경우가 있을 수 있기에)
predecessor = [] # lis_length가 update될때마다 그들의 idx와 num을 저장 [(idx, num), ..]

def binary_search(tree, target):
    start, end = 0, len(tree)-1

    while start <= end:
        mid = (start + end) // 2

        if tree[mid] < target:
            start = mid+1
        else:
            end = mid -1
    return start


for idx in range(len(arr)):
    num = arr[idx]
    if idx == 0:
        lis_length.append(num)
        predecessor.append((idx, num))
    elif lis_length[-1] < num:
        lis_length.append(num)
        predecessor.append((len(lis_length)-1, num)) #새로 맨 뒤에 추가되는거니까 lis_length의 맨 뒤 index를 받아옴
    else:
        new_idx = binary_search(lis_length, num)
        lis_length[new_idx] = num
        predecessor.append((new_idx, num))

last_idx = len(lis_length)-1
answer = []
for i in range(len(predecessor)-1, -1, -1):
    if predecessor[i][0] == last_idx:
        answer.append(predecessor[i][1])
        last_idx -= 1

print(len(answer))
print(*answer[::-1])





