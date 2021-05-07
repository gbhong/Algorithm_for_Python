# 각 축(axis)에서 한 번 등장하는 좌표 리턴 --> 시간 복잡도 문제 발생
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