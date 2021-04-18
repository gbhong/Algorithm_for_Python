import sys
sys.stdin = open("/Users/gibonghong/Downloads/input.txt", "r")

# 1267. 작업순서
from collections import defaultdict

def make_directed_graph(edges:list): # edges의 형태 -> [[1,2], [2,3]]
    graph, rev_graph = defaultdict(list), defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
        rev_graph[end].append(start)

    return graph, rev_graph

def BFS(graph, rev_graph, start):
    visited = list()
    bfs_queue = list()

    bfs_queue.append(start)

    while bfs_queue:
        curr = bfs_queue.pop(0)
        # 현재 노드가 방문한 노드에 없고, 현재 노드를 방문하기 위한 충분조건을 만족한 경우
        if curr not in visited and set(rev_graph[curr]).issubset(set(visited)):
            visited.append(curr)
            bfs_queue.extend(graph[curr])

    return visited

for test_case in range(1, 12):
    num_vertex, num_edge = map(int, input().split())
    print(test_case, num_vertex, num_edge)
    _edges = input().split()
    # print(_edges)

    edges = []
    for i in range(num_edge): # 간선의 개수가 4일때
        edges.append([_edges[2*i], _edges[2*i+1]])

    graph, rev_graph = make_directed_graph(edges)
    # print(graph, rev_graph)

    for start in range(1, num_vertex+1):
        path = BFS(graph, rev_graph, str(start))
        if len(path) == num_vertex:
            print('#{} {}'.format(test_case, ' '.join(path)))
            break