def solution(record):
    dic = {}
    for s in record:
        sp = s.split()
        if sp[0] in ['Enter', 'Change']:
            dic[sp[1]] = sp[2]

    answer = []
    for s in record:
        sp = s.split()
        if sp[0] == 'Enter':
            answer.append(f'{dic[sp[1]]}님이 들어왔습니다.')
        elif sp[0] == 'Leave':
            answer.append(f'{dic[sp[1]]}님이 나갔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))