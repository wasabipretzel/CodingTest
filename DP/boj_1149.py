"""
    i step 은 i-1 step의 각 R, G, B 를 칠했을 경우의 수에 현재 R, G, B를 각각
    update 해서 최소만 저장하기
"""

N = int(input())

cost = [[] for _ in range(N+1)]

# 1 ~ N

for i in range(1, N+1):
    R, G, B = map(int, input().split())
    cost[i].extend([R, G, B])

# cost[a][b] : a : house num, b : R/G/B -> cost
dp = [[0,0,0] for _ in range(N+1)]
dp[1][0] = cost[1][0]
dp[1][1] = cost[1][1]
dp[1][2] = cost[1][2]
# (0, 0, 0)
# dp[i][R] = min(dp[i-1][G]+cost[i][R] + dp[i-1][B]+cost[i][R])
# dp[i][G] = min(dp[i-1][R]+cost[i][G] + dp[i-1][B]+cost[i][G])
# dp[i][B] = min(dp[i-1][G]+cost[i][B] + dp[i-1][R]+cost[i][B])
# 2 ~ N
for house_num in range(2, N+1):
    dp[house_num][0] = min(dp[house_num-1][1] + cost[house_num][0], 
                           dp[house_num-1][2] + cost[house_num][0])
    
    dp[house_num][1] = min(dp[house_num-1][0] + cost[house_num][1],
                           dp[house_num-1][2] + cost[house_num][1])
    
    dp[house_num][2] = min(dp[house_num-1][0] + cost[house_num][2],
                           dp[house_num-1][1] + cost[house_num][2])

print(min(dp[N]))




