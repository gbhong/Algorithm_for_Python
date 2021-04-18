import sys
sys.stdin = open('./BJ_15686_input.txt', 'r')

N, M = map(int, input().split()) # 도시 크기는 N*N, 치킨집 최대 개수는 M

# 인접행렬 만들고 치킨가게 위치 만들기
adj_matrix = [input().split() for _ in range(N)]

house, chicken = [], []
for i in range(N):
    for j in range(N):
        if adj_matrix[i][j] == '1':
            house.append((i, j))
        if adj_matrix[i][j] == '2':
            chicken.append((i, j))

# 치킨 가게에 대해 원소를 M개로 하는 부분집합 생성
# itertools or recursive function

def powerset(arr:list, curr:list, idx:int):
    global res, M

    for i in range(idx, len(arr)):
        curr.append(arr[i])
        if len(curr) == M:
            res.append(tuple(curr))
        else:
            powerset(arr, curr, i+1)
        curr.pop()

res = []
powerset(chicken, [], 0)
print(res)

# 각 부분집합에 대해 집과의 거리를 보관하며 최소값만 남기기
answer = 99999
for t in res:
    dist = 0
    for h in house:
        k = 99999
        for c in t:
            k = min(k, abs(h[0]-c[0])+abs(h[1]-c[1]))
        dist += k
    if dist < answer:
        answer = dist
print(answer)

