# https://www.acmicpc.net/problem/1932

N = int(input())

floor = [[] for _ in range(N+1)]
data_table = []

total_cnt = 0

# breakpoint()
for _ in range(N):
    each_floor_num_list = list(map(int, input().split()))
    curr_floor = len(each_floor_num_list)
    floor[curr_floor].append(total_cnt)
    floor[curr_floor].append(total_cnt + curr_floor-1)
    total_cnt += curr_floor
    for each_num in each_floor_num_list:
        data_table.append(each_num)

dp =[0] * total_cnt

#점화식 -> dp[idx] = max(dp[idx-curr_floor] , dp[idx-curr_floor +1]) + floor[idx]
# 가장자리일 경우 비교대상이 하나만 있음 -> 만약 좌측 끝이면 st 만 참조, 우츠 ㄱ끝이면 end만 참조

dp[0] = data_table[0]

floor_idx = 2
while floor_idx < N+1:
    curr_st_idx , curr_end_idx = floor[floor_idx][0], floor[floor_idx][1]
    for each_idx in range(curr_st_idx, curr_end_idx+1):
        if each_idx == curr_st_idx: #좌측끝이면 idx-curr_floor+1만 참조
            dp[each_idx] = dp[each_idx - floor_idx+1] + data_table[each_idx]
        elif each_idx == curr_end_idx:
            dp[each_idx] = dp[each_idx-floor_idx] + data_table[each_idx]
        else:
            dp[each_idx] = max(dp[each_idx-floor_idx], dp[each_idx-floor_idx+1]) + data_table[each_idx]
    floor_idx += 1

# 마지막 floor에서 max를 pick해서 print
if N < 2:
    print(dp[0])
else:
    print(max(dp[curr_st_idx:curr_end_idx+1]))




    
    

