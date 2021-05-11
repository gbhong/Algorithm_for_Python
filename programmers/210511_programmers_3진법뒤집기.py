def solution(n):
    k = ''
    while n >= 3:
        q, r = divmod(n, 3)
        k += str(r)
        n = q
    k += str(n)

    answer = 0
    for i in range(len(k)):
        answer += int(k[i])*3**(len(k)-i-1)
    return answer