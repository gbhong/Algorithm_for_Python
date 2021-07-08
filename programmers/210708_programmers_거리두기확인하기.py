# BFS + SIMULATION (45m)
from collections import deque

def solution(places):
    answer = []
    for room in places: # 각 방마다 검사
        answer.append(room_check(room))
    return answer # [1,0,0,0,1]

def room_check(room):
    # 방마다 사람 앉은 좌표 저장
    res = []
    for i in range(5):
        for j in range(5):
            if room[i][j] == 'P':
                res.append((i,j))

    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    for px, py in res: # 모든 P 좌표에 대해 체크
        visited = [[0] * 5 for _ in range(5)] # [[0, 0, 0, 0, 0],[0, 0, 1, 0 ,0]...[]]
        visited[px][py] = 1 # 출발시에 방문 체크
        queue = deque() # BFS
        queue.append((px,py)) # px, py -> 출발지점
        while queue:
            cx, cy = queue.popleft() # 탐색 시작 지점
            if visited[cx][cy] == 3: # 맨해튼 거리가 2 이하에만 검사 필요
                break # 다음 P 검사
            for i in range(4): # 상하좌우 탐색
                if (0 <= cx + dx[i] < 5) and (0 <= cy + dy[i] < 5) and room[cx+dx[i]][cy+dy[i]] != 'X' and visited[cx+dx[i]][cy+dy[i]] == 0:
                    if room[cx+dx[i]][cy+dy[i]] == 'P':
                        return 0 # 수칙위반 걸리는 순간 종료
                    else: # 사람이 앉지 않은 빈 자리일때
                        visited[cx+dx[i]][cy+dy[i]] = visited[cx][cy] + 1
                        queue.append((cx+dx[i], cy+dy[i]))
    return 1 # 전원 통과

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
