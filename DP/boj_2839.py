# https://www.acmicpc.net/problem/2839
"""
    N = 5 * x + 3 * y
    -> 5의 몫과 나머지를 먼저 구하고, 나머지가 3으로 처리가 안된다면
    x-1 을 해본다. 

    만약 x 가 0인데도 처리가 안된다면 -1을 return
"""

N = int(input())


x = N // 5
leftover = N % 5

flag = True
while flag:
    if x == -1:
        flag = False
    elif leftover % 3 == 0:
        y = leftover // 3
        flag = False
    else:
        x -= 1
        leftover += 5

if x == -1:
    print(-1)
else:
    print(x + y)
