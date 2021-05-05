def solution(n):
    a, b = 0, 1

    i = 1
    while i < n:
        a, b = b, a+b # DP로 접근
        i += 1
    return b % 1234567

print(solution(5))