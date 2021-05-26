# # BFS
# from collections import deque
#
# def solution(numbers, target):
#     queue = deque()
#     queue.append((0, 0))
#
#     answer = 0
#     while queue:
#         k, idx = queue.popleft()
#         if idx == len(numbers):
#             if k == target:
#                 answer += 1
#         else:
#             queue.append((k + numbers[idx], idx + 1))
#             queue.append((k - numbers[idx], idx + 1))
#
#     return answer

# 점화식을 이용한 풀이
def solution(numbers, target):
    if numbers == []:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return solution(numbers[1:], target-numbers[0]) \
               + solution(numbers[1:], target+numbers[0])

print(solution([1,1,1,1,1], 3))