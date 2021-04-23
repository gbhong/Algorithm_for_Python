import sys
sys.stdin = open('./BJ_16236_input.txt', 'r')

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            start = (i, j)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

size = 2 # 아기상어 사이즈
cnt = 0 # 먹은 물고기 개수 측정

def BFS(start:tuple):
    global graph, dx, dy, cnt, size, eat, cnt_path

    visited = [[0]*N for _ in range(N)]
    visited[start[0]][start[1]] = 1  # 걸린 시간 측정

    points = []; len_path = -1 # 같은 거리에 위치한 노드들의 좌표를 sort해야 함
    queue = [start]
    while queue:
        cx, cy = queue.pop(0)
        if len_path == visited[cx][cy]: # 식사 시작

            points.sort(key=lambda x:(x[0], x[1]))
            print(points)
            cnt += 1  # 먹은 개수
            if cnt == size:
                size += 1
                cnt = 0  # reset

            ex, ey = points[0]
            graph[ex][ey] = 0

            return ((ex, ey), len_path-1) # 조건에 부합하는 최단거리의 먹이 먹고 종료

        for i in range(4):
            nx = cx + dx[i]; ny = cy + dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and (visited[nx][ny] == 0) and (graph[nx][ny] <= size):
                visited[nx][ny] = visited[cx][cy] + 1  # 물고기의 사이즈가 크지만 않으면 지나갈 수 있다
                queue.append((nx, ny)) # 다음 이동 지점 추가

                if 1 <= graph[nx][ny] < size: # 물고기 먹을 수 있는 조건이면 points에 담기
                    len_path = visited[nx][ny]
                    points.append((nx, ny))
    return -1

ans = 0
while True:
    result = BFS(start)
    if result == -1: # 엄마 상어 호출
        print(ans)
        break
    else: # 먹이 찾아나서기
        ans += result[1]
        start = result[0]