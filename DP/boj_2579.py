N = int(input())

stair_list = []
for _ in range(N):
    value = int(input())
    stair_list.append(value)


"""
    블로그들에는 마지막 칸을 밟아야하니까 역으로 설계하는데 그건 모르겠고...
    table을 그렸을때, 처음에 O , X 로 한 후, 경우의 수대로 뻗어나가다보면,
    가장 작은 X은 계속 이어나가봤자 최댓값이 될 수 없음. (어차피 더 큰 x에 다음 숫자를 동등하게 더하면 더 커지기 때문)

    따라서 매 분기마다 "이전에 밟았던 경우 : o" , "이전을 밟지 않은 경우 중 가장 큰 것 : x", "이이전, 이전 밟은 경우 : oo "
    이렇게 3개만 들고 다니면 된다. -> 마지막에 그 중 최대 찾기
"""

past_cache = []
idx = 0

# first case
curr_cache = []
curr_cache.append(("o", stair_list[idx]))
curr_cache.append(("x", 0))
past_cache = curr_cache
curr_cache = []
idx += 1


while idx < N-1:
    max_x = -1
    for each_pair in past_cache:
        if each_pair[0] == "o":
            curr_cache.append(("oo", stair_list[idx] + each_pair[1]))
            # 다음이 x인경우 비교 필요
            if max_x != -1:
                max_x = max(max_x, each_pair[1])
            else:
                max_x = each_pair[1]
        elif each_pair[0] == "x":
            curr_cache.append(("o", stair_list[idx] + each_pair[1]))
        elif each_pair[0] == "oo":
            if max_x != -1:
                max_x = max(max_x, each_pair[1])
            else:
                max_x = each_pair[1]
        else:
            raise ValueError
        
    curr_cache.append(("x", max_x))
    past_cache = curr_cache
    curr_cache = []
    idx += 1


# idx 맨 마지막 -> 무조건 O해야함
result = -1
for each_pair in past_cache:
    if each_pair[0] != "oo":
        if N == 1:
            result = max(result, each_pair[1]) # N 이 1인경우는 이렇게 해줘야함
        else:
            result = max(result, each_pair[1]+stair_list[idx])

print(result)



