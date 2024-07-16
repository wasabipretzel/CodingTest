# https://www.acmicpc.net/problem/1717

"""
    Union Find 문제
    1. 집합을 어떻게 나타낼 것인가? -> 1차원 배열 사용
    2. Union 연산
    3. Find 연산

    4. 효율을 위한 경로 압축 -> 경로압축이란?
    # union연산 시 대표 노드끼리만 연결. 기타는 find연산에서 경로압축을 통해 달성
    # 집합의 대표 노드는 가장 작은 노드 ㅇㅇ
"""


n, m = map(int, input().split()) # n : 0 ~ n 의 초기 집합 (total n+1개) , m : 연산의 수

graph = [0]*(n+1) # index가 속한 집합의 대표 노드가 어떤 것인지를 기록

test_cases = []
for _ in range(m):
    type, a, b = map(int, input().split())
    test_cases.append([type, a, b])
    # type이 0이면 합집합 연산
    # type이 1이면 두 원소가 같은 집합에 포함되는지

def union(a, b):
    """
        특정 2개의 노드를 연결해 1개의 집합으로 묶어준다
        => 노드가 속한 집합의 대표 노드를 찾아서 연결
    :return: 
    """
    p_a, p_b = find(a), find(b)
    if p_a < p_b: #더 작은 대표 노드가 합집합의 대표 노드가 됨
        graph[p_b] = p_a #NOTE 대표 노드 끼리 연결해야함
    else:
        graph[p_a] = p_b
    return

def find(a):
    """
        두 노드가 같은 집합에 속해 있는지를 확인하기 위해
        -> 노드가 속해있는 집합의 대표 노드를 찾는 연산
        #NOTE 궁금: 여기서 이전 노드들의 대표노드를 update해주면
        union 연산 이후에 find를 하면 O(1)이 아니라 한번 더 올라가야하지않나?

        index와 value 가 같지 않다 -> 거슬러 올라가
        만약 둘이 같다 -> 그게 대표 노드임
        # 대표노드를 찾으면 재귀를 빠져나오면서 같은 집합의 노드들의 대표 값을 찾은 대표 노드로 바꿔야함 -> 경로압축
    :return: 
    """
    stack = []
    while graph[a] != a:
        stack.append(a)
        a = graph[a] #거슬러 올라감

    # index와 value가 같은 시점 -> 이때 a가 대표노드
    # 이전에 거쳐온 노드들의 대표 노드를 수정해준다 -> 경로압축
    while stack:
        previous_node = stack.pop()
        graph[previous_node] = a
    return a


# 초기화 -> 자기 자신을 대표 노드로 우선 설정
for i in range(n+1):
    graph[i] = i


for each_case in test_cases:
    type, a, b = each_case
    if type == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

