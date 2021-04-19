import sys
sys.stdin = open('./BJ_14503_input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # (r,c)는 시작 위치, d는 방향
graph = [list(map(int, input().split())) for _ in range(N)] # 행의 개수만큼 loop

def DFS(start:tuple):
    global graph
    stack = [start]

    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    move = [(-1,0),(0,1),(1,0),(0,-1)]

    while stack:
