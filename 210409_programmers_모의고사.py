def match_ans(answer:list, user:list):
    n = len(user)
    k = 0
    for idx in range(len(answer)):
        if answer[idx] == user[idx%n]:
            k += 1
    return k

def solution(answers:list):
    # define patterns
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]

    _user = [] # 유저별 정답 개수
    for user in a,b,c: # 이중 배열
        _user.append(match_ans(answers, user))

    _user = [1,3,5] # 유저별 정답 개수

    _user_sorted = sorted(list(enumerate(_user, start=1)), key = lambda x: (-x[1], x[0])) # 수포자 번호와 정답 개수를 담은 리스트
    return [user for user, score in _user_sorted if score == _user_sorted[0][1]]

print(solution([1,3,2,4,2]))