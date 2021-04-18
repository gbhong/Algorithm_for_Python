import sys
sys.stdin = open('./BJ_2589_input.txt', 'r')

from collections import deque

# L로 표시된 점마다 거리 계산
def BFS(start:tuple):
    global graph, M, N

    queue = deque()
    queue.append(start)

    visited = [[0]*len(graph[0]) for _ in range(len(graph))]
    visited[start[0]][start[1]] = 1

    # 상하좌우 움직이기
    move = [(-1,0),(1,0),(0,1),(0,-1)]

    maxi = 0
    while queue:
        curr = queue.popleft() # curr는 좌표를 담은 tuple

        for m in move: # 상하좌우 이동
            v = (curr[0]+m[0], curr[1]+m[1])
            if (0 <= v[0] < M) & (0 <= v[1] < N):
                if (graph[v[0]][v[1]] == 'L') & (visited[v[0]][v[1]] == 0): # 아직 가지 않은 점을 방문하는 순간 해당 점까지의 최단거리 업데이트
                    queue.append(v)
                    visited[v[0]][v[1]] = visited[curr[0]][curr[1]] + 1
                    maxi = max(maxi, visited[v[0]][v[1]]) # 최단거리 업데이트

    return maxi-1

M, N = map(int, input().split())

# 인접행렬 만들기
graph = []
for _ in range(M):
    graph.append(list(input()))

# 그래프 내 L 노드에서 최대 거리 구하기
answer = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 'L':
            answer = max(answer, BFS(start=(i,j)))

print(answer)