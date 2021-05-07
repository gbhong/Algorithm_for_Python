# dict 자료구조에서 pointer 활용
def solution(gems):
    size = len(set(gems))
    dic = {gems[0]:1}
    ans = [0, len(gems)-1]
    start, end = 0, 0

    while start < len(gems):
        if len(dic) == size:
            if (end - start) < (ans[1] - ans[0]):
                ans = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems): # 포인터가 배열 이탈하면 종료
                break
            if gems[end] in dic:
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1

    return [ans[0]+1, ans[1]+1]