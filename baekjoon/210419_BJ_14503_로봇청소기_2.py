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
dy = [0,-1,0,1]
rotation = [3,0,1,2]

cnt = 1
while True:
    for i in range(4):
        nx = r + dx[i]; ny = c + dy[i]
        if (0 <= nx < M) and (0 <= ny < N) and visited[nx][ny] == 0:
            d = rotation[i]
            r = nx; c = ny
            cnt += 1
            break

