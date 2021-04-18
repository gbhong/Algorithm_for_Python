import sys
sys.stdin = open("/Users/gibonghong/Downloads/sample_input.txt", "r")

# 5521. 상원이의 생일파티

def make_adj(adj:dict, key1: str, key2: str):
    if key1 not in adj:
        adj[key1] = [key2]
    else:
        adj[key1].append(key2)
    return adj

def BFS(adj: dict, start: str):
    bfs_queue = [(start, 0)]
    visited = set()

    while bfs_queue:
        curr, degree = bfs_queue.pop(0)
        if degree >= 3: # 친구의 친구면 탐색 중단
            pass
        else:
            if curr not in visited:
                visited.add(curr)
                for n in adj[curr]:
                    bfs_queue.append([n, degree+1])

    return visited

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    # 인접 그래프 만들어주기
    adj = dict()
    for _ in range(M):
        f1, f2 = input().split()
        adj = make_adj(adj, f1, f2)
        adj = make_adj(adj, f2, f1)

    if '1' not in adj:
        print(f'#{test_case} 0')
    else:
        answer = BFS(adj, start='1')
        print(f'#{test_case} {len(answer)-1}')