def solution(v):
    x = [p[0] for p in v]
    y = [p[1] for p in v]

    answer = [0, 0]
    for i in range(len([x,y])):
        for p in [x,y][i]:
            if [x,y][i].count(p) == 1:
                answer[i] = p
                break

    return answer

print(solution([[1,4],[3,4],[3,10]]))