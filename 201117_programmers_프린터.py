def solution(priorities, location):
    lst = list(enumerate(priorities))

    answer = 0
    while True:
        item = lst.pop(0) # item = [0,1]
        if len(lst) == 0 or item[1] >= max(lst, key=lambda x: x[1])[1]:
            answer += 1
            if item[0] == location:
                return answer
        else:
            lst.append(item)

print(solution([1,1,9,1,1,1], 0))

# 문제1 -> 프린터 -> 1시간 반?
# 문제2 -> 합
