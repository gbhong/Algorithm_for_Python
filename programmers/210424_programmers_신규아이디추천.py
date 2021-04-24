def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for s in new_id:
        if s.isalpha() or s.isdigit() or s in ['-','_','.']:
            answer += s
    # 3
    while '..' in answer: # 2개 이상 문자열을 없애고자 할 때
        answer = answer.replace('..', '.')
    # 4
    answer = answer.strip('.')
    # 5
    if not answer:
        answer = 'a'
    # 6
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')
    # 7
    elif len(answer) <= 2:
        s = answer[-1]
        while len(answer) < 3:
            answer += s
    return answer

print(solution('abcdefghijklmn.p'))