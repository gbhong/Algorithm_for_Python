import math

def combi(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def solution(n):
    answer = 0
    q = n // 2
    if n%2 == 0:
        for i in range(q, -1, -1):
            answer += combi((2*q)-i, i)
    else:
        for i in range(q, -1, -1):
            answer += combi((2*q+1)-i, i)

    return answer%1234567

# def solution(n):
#     if n <= 2:
#         return n
#     else:
#         return (solution(n-1) + solution(n-2))%1234567

print(solution(2000))