def solution(A:list, B:list):
    A.sort(reverse=True) # 내림차순
    B.sort(reverse=True) # 내림차순

    answer = 0
    while A:
        num = A.pop(0)

        i = 0
        while True:
            if num >= B[i]:
                break
            else:
                i += 1
                if i == len(B):
                    break

        if 0 < i <= len(B):
            B.pop(i-1)
            answer += 1

    return answer

print(solution([5,1,3,7], [2,2,6,8]))

# 7 5 3 1
# 9 8 2 2