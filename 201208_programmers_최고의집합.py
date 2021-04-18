answer = []

# # python에서 재귀 1000번 이상 돌면 런타임 에러 발생
# def solution(n, s):
#     if n > s:
#         return [-1]
#     else:
#         if n == 1:
#             answer.append(s)
#             answer.sort()
#             return answer
#         else:
#             q = s//n
#             answer.append(q)
#             return solution(n-1, s-q)

# 재귀 대신 while문
def solution(n, s):
    if n > s:
        return [-1]
    else:
        answer = []
        while n > 1:
            q = s//n
            answer.append(q)
            n -= 1
            s -= q
        answer.append(s)
        return answer


print(solution(787, 89839444))