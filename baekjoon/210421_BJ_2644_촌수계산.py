import sys
sys.stdin = open('./BJ_2644_input.txt', 'r')

# 풀이에 걸린 시간: 25~30분

N = int(input())
graph = [[0]*N for _ in range(N)]

s, t = map(int, input().split())
s -= 1; t -= 1

num_rel = int(input())
for _ in range(num_rel):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1; graph[y-1][x-1] = 1

visited = [0]*N
visited[s] = 1

def BFS(start:int, target:int):
    global visited

    queue = [start]
    valid = 0
    while queue:
        curr = queue.pop(0)
        for v in range(N):
            if (graph[curr][v] == 1) and (visited[v] == 0):
                visited[v] = visited[curr] + 1
                queue.append(v)
                if v == target:
                    valid = 1
                    return visited[v] - 1
    if valid == 0:
        return -1

print(BFS(start=s, target=t))