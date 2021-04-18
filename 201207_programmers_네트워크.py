def DFS(graph, idx_start):
    visited = [0]*len(graph)
    path = []

    dfs_stack = []
    dfs_stack.append(idx_start)
    path.append(idx_start)
    visited[idx_start] = 1

    while dfs_stack:
        for idx, val in enumerate(graph[dfs_stack[-1]]): # LIFO
            if val and not visited[idx]:
                dfs_stack.append(idx)
                path.append(idx)
                visited[idx] = 1
                break
        else:
            dfs_stack.pop()

    return path

def solution(n, computers):
    answer = []
    for i in range(n):
        result = DFS(computers, i)

        result.sort()
        if result not in answer:
            answer.append(result)

    return len(answer)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))