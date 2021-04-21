import sys
sys.stdin = open('./BJ_14503_input.txt', 'r')

N, M = map(int, input().split()) # N은 행의 개수, M은 열의 개수
r, c, d = map(int, input().split()) # (r,c)는 시작 위치, d는 방향
graph = [list(map(int, input().split())) for _ in range(N)] # 행의 개수만큼 loop

visited = [[0]*M for _ in range(N)]
visited[r][c] = 1

rotated = [0, 0, 0, 0]

clean = 1
while True:
    if d == 0: # heads to North
        d = 3; rotated[3] += 1  # rotates to West
        if (c-1 >= 0) and (graph[r][c-1] == 0) and (visited[r][c-1] == 0): # 조건 만족 시 청소하기
            visited[r][c-1] = 1
            clean += 1
            c -= 1; rotated = [0,0,0,0]
        else:
            if sum(rotated) == 4:  # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
                if (c+1 >= M) or graph[r][c+1] == 1:
                    print(clean)
                    break
                else:
                    c += 1; rotated = [0,0,0,0] # 후진

    elif d == 1: # heads to East
        d = 0; rotated[0] += 1  # rotates to North
        if (r-1 >= 0) and (graph[r-1][c] == 0) and (visited[r-1][c] == 0):
            visited[r-1][c] = 1
            clean += 1
            r -= 1; rotated = [0,0,0,0]
        else:
            if sum(rotated) == 4:
                if (r+1 >= N) or graph[r+1][c] == 1:
                    print(clean)
                    break
                else:
                    r += 1; rotated = [0,0,0,0]

    elif d == 2: # heads to South
        d = 1; rotated[1] += 1  # rotates to East
        if (c+1 < M) and (graph[r][c+1] == 0) and (visited[r][c+1] == 0):
            visited[r][c+1] = 1
            clean += 1
            c += 1; rotated = [0,0,0,0]
        else:
            if sum(rotated) == 4:
                if (c-1 < 0) or graph[r][c-1] == 1:
                    print(clean)
                    break
                else:
                    c -= 1; rotated = [0,0,0,0]

    else: # heads to West
        d = 2; rotated[2] += 1  # rotates to South
        if (r+1 < N) and (graph[r+1][c] == 0) and (visited[r+1][c] == 0):
            visited[r+1][c] = 1
            clean += 1
            r += 1; rotated = [0,0,0,0]
        else:
            if sum(rotated) == 4:
                if (r-1 < 0) or graph[r-1][c] == 1:
                    print(clean)
                    break
                else:
                    r -= 1; rotated = [0,0,0,0]