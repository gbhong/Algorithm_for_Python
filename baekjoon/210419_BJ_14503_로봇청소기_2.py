# 간결하게 풀어보기
import sys
sys.stdin = open('./BJ_14503_input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
visited[r][c] = 1

dx = []
dy = []

clean = 1
while True:
    for i in range(4):
