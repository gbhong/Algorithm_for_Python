Q = [[1,2],[1,4],[1,6],[2,3],[3,7],[4,5],[4,9],[6,8]]

def make_adj(adj:dict, key1: str, key2: str):
    if key1 not in adj:
        adj[key1] = [key2]
    else:
        adj[key1].append(key2)
    return adj

def BFS(adj:dict, start:int):
    bfs_queue = [(start, 0)] # node와 depth=0를 같이 저장
    visited, result = [], []

    k = 0
    while bfs_queue:
        curr, depth = bfs_queue.pop(0)
        if curr not in visited:
            visited.append(curr)
            result.append((curr, depth))

            for node in adj[curr]:
                bfs_queue.append((node, depth+1))

    result.sort(key=lambda x: [x[1], x[0]])
    result = [node for node, depth in result]
    return result

# 인접 그래프 만들기
adj = dict()
for n1, n2 in Q:
    adj = make_adj(adj, n1, n2)
    adj = make_adj(adj, n2, n1)

answer = BFS(adj, start=1)
print(answer)
