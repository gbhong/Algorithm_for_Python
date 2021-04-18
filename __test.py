def solution(priorities, location):
    importance = max(priorities)

    p_l = []
    for i in range(0, len(priorities)):
        p_l.append([i, priorities[i]])

    new_p_l = []
    while len(new_p_l) < len(priorities) - 1:
        if p_l[0][1] == importance:
            new_p_l.append(p_l[0])
            del (p_l[0])
            importance = max(p_l, key=lambda x: x[1])[1]

        else:
            p_l.append(p_l[0])
            del (p_l[0])

    new_p_l.append(p_l[0])

    check = 1
    for i in new_p_l:
        if i[0] == location:
            answer = check
            break;
        check += 1

    return answer

print(solution([1,1,9,1,1,1], 0))