# 간결하게 풀어보기
import sys
sys.stdin = open('./BJ_14503_input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
visited[r][c] = 1

# d가 0인 경우 북, 1인 경우 동, 2인 경우 남, 3인 경우 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def clean(r, c, d):
    global N, M, graph, visited, cnt
    for i in range(d+3, d-1, -1):
        i %= 4 # 방향 회전
        nx = r + dx[i]; ny = c + dy[i] # 다음 위치 설정
        if (graph[nx][ny] == 0) and (visited[nx][ny] == 0): # 다음 위치 이동 가능 여부
            visited[nx][ny] = 1; cnt += 1
            return nx, ny, i

    # 네 방향 모두 청소 실패했을 때, 후진 가능 여부 판단
    bx = r - dx[i]; by = c - dy[i]
    if graph[bx][by] == 0:
        return bx, by, d
    else:
        return -1

cnt = 1
while True:
    result = clean(r, c, d)
    if result == -1:
        print(cnt)
        break
    else:
        r, c, d = result[0],result[1],result[2]
