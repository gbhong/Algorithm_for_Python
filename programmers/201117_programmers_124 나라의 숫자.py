def solution(n):
    num = '412'
    answer = ''

    if n in [1, 2, 3]:
        return num[n%3]

    else:
        while n > 0:
            s, r = divmod(n, 3)
            answer += num[r]

            if r == 0:
                s -= 1
            n = s

            if n <= 3:
                break

        answer += num[n % 3]

        return answer[-1::-1]

print(solution(10))