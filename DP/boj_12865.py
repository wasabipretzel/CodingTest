# https://www.acmicpc.net/problem/12865 DP문제

# K : 배낭 최대 무게
# obj : sum V의 최대화
# s.t : sum W <= K

"""
    DP문제는
    1. Table을 노가다로 다 만들어본다
    2. 노가다로 만들때 어떻게 만들었는지를 통해 매 cell을 채울 점화식을 찾는다
    3. 그 table을 점화식으로 구현한다.
"""


N, K = map(int, input().split())

# 행은 object 종류
# 열은 배낭의 무게 (0kg ~ K kg) 까지
dp = [[0]*(K+1) for _ in range(N)]

weights = []
values = []

for _ in range(N):
    W, V = map(int, input().split())
    weights.append(W)
    values.append(V)


#start
# 첫번째 행의 경우에는 이전이 없으니 그냥 다 0으로..?
for i in range(N):
    for j in range(K+1):
        if i == 0: #첫 번째 행 채우기
            if j >= weights[i]:
                dp[i][j] = values[i]
            else:
                dp[i][j] = 0
        else:
            # 만약 조회해야하는 index 가 음수인경우에는 그냥 table 0
            if j - weights[i] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])
            else:
                dp[i][j] = dp[i-1][j]
        # print(dp)

print(max(dp[N-1]))
