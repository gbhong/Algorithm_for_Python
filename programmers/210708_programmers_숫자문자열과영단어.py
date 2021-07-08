# 단순 구현(12m)

def solution(s):
    dic = {'zero':'0','one':'1','two':'2','three':'3','four':'4',
           'five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

    answer, temp = '', ''
    for char in s:
        if char in '0123456789':
            answer += char
        else:
            temp += char
            if temp in dic:
                answer += dic[temp]
                temp = ''
    return int(answer)

print(solution("one4seveneight"))

# 14:13
