from collections import defaultdict

def BFS_path(graph, begin, target):
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

def make_adj(words):
    adj_list = defaultdict(list)

    for i in range(len(words)): # 3중 for문...
        for j in range(i + 1, len(words)):
            cnt = 0
            for k in range(len(words[0])):
                if words[i][k] == words[j][k]:
                    cnt += 1
            if cnt == len(words[0]) - 1:
                adj_list[words[i]].append(words[j])
                adj_list[words[j]].append(words[i])

    return adj_list

def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        words.append(begin) # 시작점도 추가해서 인접 리스트 만들기
        adj_list = make_adj(words)
        answer = BFS_path(adj_list, begin, target)

        if len(answer) == 0:
            return 0
        else:
            return len(answer)[0] - 1

begin = 'hit'
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

print(solution(begin, target, words))