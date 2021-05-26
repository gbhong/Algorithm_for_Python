# BFS
from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append((0, 0))

    answer = 0
    while queue:
        k, idx = queue.popleft()
        if idx == len(numbers):
            if k == target:
                answer += 1
        else:
            queue.append((k + numbers[idx], idx + 1))
            queue.append((k - numbers[idx], idx + 1))

    return answer

print(solution([1,1,1,1,1], 3))