import sys
sys.stdin = open('./BJ_16236_input.txt', 'r')

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            start_x, start_y = i, j

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

size = 2 # 아기상어 사이즈
cnt = 0 # 먹은 물고기 개수 측정

def BFS(start:tuple):
    global graph, dx, dy, cnt, size, eat

    visited = [[0]*N for _ in range(N)]
    visited[start[0]][start[1]] = 1  # 걸린 시간 측정

    queue = [start]
    while queue:
        cx, cy = queue.pop(0)
        for i in range(4):
            nx = cx + dx[i]; ny = cy + dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and (visited[nx][ny] == 0) and (graph[nx][ny] <= size):
                queue.append((nx, ny)) # 다음 이동 지점 추가
                visited[nx][ny] = visited[cx][cy] + 1 # 물고기의 사이즈가 크지만 않으면 지나갈 수 있다

                if 1 <= graph[nx][ny] < size: # 물고기 먹을 수 있는 조건 --> 최단거리 먹이가 같은 거리에 2개 이상 있으면 비교 --> 먹고 나서 새롭게 출발
                    cnt += 1 # 먹은 개수
                    if cnt == size:
                        size += 1
                        cnt = 0 # reset

                    graph[nx][ny] = 0
                    return (nx, ny, visited[nx][ny]-1) # 최단거리의 먹이 먹고 종료
    return -1

ans = 0
while True:
    result = BFS((start_x, start_y))
    if result == -1: # 엄마 상어 호출
        print(ans)
        break
    else: # 먹이 찾아나서기
        ans += result[2]
        start_x, start_y = result[0], result[1]