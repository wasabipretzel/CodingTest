# https://www.acmicpc.net/problem/11659


N, M = map(int, input().split())

arr = list(map(int, input().split()))

test_cases = []

for _ in range(M):
    A, B = map(int, input().split())
    test_cases.append([A, B])

sum_arr = [-1 for _ in range(N)]

sum_arr[0] = arr[0]

for i in range(1, len(arr)):
    sum_arr[i] = sum_arr[i-1] + arr[i]

# print(sum_arr)

for each_case in test_cases:
    A, B = each_case
    if A == B:
        print(arr[A-1])
    else:
        print(sum_arr[B-1] - sum_arr[A-1] + arr[A-1])
