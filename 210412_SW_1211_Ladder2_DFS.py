import sys
sys.stdin = open("/Users/gibonghong/Downloads/input.txt", "r")

def DFS(start:tuple):
    global adj_matrix
    stack = [start]
    visited = [[0]*100 for _ in range(100)]
    visited[start[0]][start[1]] = 1

    # 좌, 우, 하로의 움직임만 가능 -> 아래, 왼쪽, 오른쪽 순으로 넣어준다
    move = [(1,0),(0,-1),(0,1)]
    while stack:
        curr = stack.pop()

        for m in move:
            v = (curr[0]+m[0], curr[1]+m[1])
            if (0 <= v[0] < 100) & (0 <= v[1] < 100):
                if (adj_matrix[v[0]][v[1]] == '1') & (visited[v[0]][v[1]] == 0):
                    stack.append(v)
                    visited[v[0]][v[1]] = visited[curr[0]][curr[1]] + 1

                    if v[0] == 99:
                        return visited[v[0]][v[1]] - 1

# Assign test cases
for tc in range(1, 11):
    _ = input()

    # 주어진 100*100 2차원 평면에 맞는 인접행렬 생성
    adj_matrix = [input().split() for _ in range(100)]

    # 출발점 별로 검사
    answer = (0, 100000)
    for j in range(99,-1,-1):
        if adj_matrix[0][j] == '1':
            path = DFS(start=(0,j))
            if path < answer[1]:
                answer = (j, path)

    print(f'#{tc} {answer[0]}')
