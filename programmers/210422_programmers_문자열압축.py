def solution(s):
    answer = len(s)
    for window_size in range(1, (len(s)//2)+1):
        s2 = s[:]
        res = 0
        while s2:
            if len(s2) < window_size:
                res += len(s2)
                break
            else:
                sp, s2 = s2[:window_size], s2[window_size:]
                cnt = 1
                while True:
                    if sp == s2[:window_size]:
                        cnt += 1
                        s2 = s2[window_size:]
                    else:
                        break
                if cnt > 1:
                    res += len(str(cnt)+sp)
                else:
                    res += len(sp)
        answer = min(res, answer)
    return answer

print(solution('abcabcab'))