# https://www.acmicpc.net/problem/12852

"""

    
"""


N = int(input())


# 1. 특정 value일 때 minimum 연산횟수를 dp로 저장해놓는다

dp = [0]*1000001

for i in range(2, N+1):
    
    dp[i] = dp[i-1] + 1

    if i % 2 ==0:
        dp[i] = min(dp[i], dp[i //2]+1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])



# 2. 역으로 N부터 1로 갈때까지 1에서 구해놓은 
# minimum 연산횟수를 따져가며 숫자를 찾는다
result = []
operation_num = dp[N]
now = N


# 위에서 1번연산할 때 여러 연산 간 중복이 안되는지 확인해볼것..
# dp[i] == operation_num 이면서 (왜냐하면 계속 +1 더했던 연산이 남아있을 것이기 때문에 now라는 변수로 변수도 최신화해줘야함)
# 즉, 특정 minimum 연산 횟수를 만족함과 동시에 
for i in range(N, 0, -1):
    if i == N:
        result.append(i)
        operation_num -=1
    elif dp[i] == operation_num and (i+1 == now or i*2 ==now or i*3 == now):
        now = i
        result.append(i)
        operation_num -=1
    else:
        pass


print(*result)
