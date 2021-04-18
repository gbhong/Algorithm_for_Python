from collections import defaultdict

def make_adj(edge): # 그래프 구현
    adj_lst = defaultdict(list)
    for n1, n2 in edge:
        adj_lst[n1].append(n2)
        adj_lst[n2].append(n1)
    return adj_lst

def BFS_path(graph, begin, target): # 경로 찾기 # visited 만들어서 풀어보기
    bfs_queue = [(begin, [begin])]
    result = []

    while bfs_queue:
        node, path = bfs_queue.pop(0)
        if node == target:
            result.append(path)
            break
        else:
            for v in set(graph[node]) - set(path):
                bfs_queue.append((v, path + [v]))

    return result

def solution(n, edge):
    graph = make_adj(edge)
    answer = 0; k = 0

    for node in range(2, n + 1):
        dist = len(BFS_path(graph, 1, node)[0])  # result가 비었다면?
        if dist > k:
            k = dist
            answer = 1  # reset answer
        elif dist == k:
            answer += 1

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))