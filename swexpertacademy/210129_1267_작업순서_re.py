import sys
sys.stdin = open("/Users/gibonghong/Downloads/input.txt", "r")

# 1267. 작업순서

from collections import defaultdict

def make_graph(edges:list): # edges의 형태 -> [[1,2], [2,3]]
    graph = defaultdict(list)
    for start, end in edges:
        graph[end].append(start)
    return graph

for test_case in range(1,11):
    num_vertex, num_edge = map(int, input().split())
    # print(test_case, num_vertex, num_edge)
    _edges = input().split()


    edges = []
    for i in range(num_edge): # 간선의 개수가 4일때
        edges.append([_edges[2*i], _edges[2*i+1]])

    graph = make_graph(edges)

    visited = []
    queue = list(range(1, num_vertex+1))
    while queue:
        curr = str(queue.pop(0))
        if curr not in visited and set(graph[curr]).issubset(set(visited)):
            visited.append(curr)
        else:
            queue.append(curr)
    print('#{} {}'.format(test_case, ' '.join(visited)))



