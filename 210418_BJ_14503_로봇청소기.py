import sys
sys.stdin = open('./BJ_14503_input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # (r,c)는 시작 위치, d는 방향
graph = [list(map(int, input().split())) for _ in range(N)] # 행의 개수만큼 loop

visited = [[0]*M for _ in range(N)]
visited[r][c] = 1

rotated = [0, 0, 0, 0]
rotated[d] = 1

clean = 1
while True:
    if d == 0: # heads to North
        d = 3; rotated[3] += 1  # rotates to West
        if (graph[r][c-1] == 0) and (visited[r][c-1] == 0): # 조건 만족 시 청소하기
            visited[r][c-1] = 1
            clean += 1
            c -= 1; rotated = [0,0,0,0]
        else:
            if sum(rotated) > 4:  # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
                d = 0 # 방향 원복
                if (r+1 >= M) or (graph[r+1][c] == 1):
                    print(clean)
                    break
                else:
                    d = 3; r += 1; rotated = [1,0,0,0] # 북 -> 남 후진

    elif d == 1: # heads to East
        d = 0; rotated[0] += 1  # rotates to North
        if (graph[r-1][c] == 0) and (visited[r-1][c] == 0):
            visited[r-1][c] = 1
            clean += 1
            r -= 1; rotated = [0,0,0,0]
        else:
            if sum(rotated) > 4:  # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
                d = 1
                if (c-1 < 0) or (graph[r][c-1] == 1):
                    print(clean)
                    break
                else:
                    d = 0; c -= 1; rotated = [0,1,0,0] # 동 -> 서 후진

    elif d == 2: # heads to South
        d = 1; rotated[1] += 1  # rotates to East
        if (graph[r][c+1] == 0) and (visited[r][c+1] == 0):
            visited[r][c+1] = 1
            clean += 1
            c += 1; rotated = [0,0,0,0]
        else:
            if sum(rotated) > 4:  # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
                d = 2
                if (r-1 < 0) or (graph[r-1][c] == 1):
                    print(clean)
                    break
                else:
                    d = 1; r -= 1; rotated = [0,0,1,0] # 남 -> 북 후진

    else: # heads to West
        d = 2; rotated[2] += 1  # rotates to South
        if (graph[r+1][c] == 0) and (visited[r+1][c] == 0):
            visited[r+1][c] = 1
            clean += 1
            r += 1; rotated = [0,0,0,0]
        else:
            if sum(rotated) > 4:  # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
                d = 3
                if (c+1 >= M) or (graph[r][c+1] == 1):
                    print(clean)
                    break
                else:
                    d = 2; c += 1; rotated = [0,0,0,1] # 서 -> 동 후진