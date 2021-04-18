# 시간계산 함수 정의
def time_cal(time1, time2):
    return int(time2[3:]) - int(time1[3:]) + (int(time2[:2]) - int(time1[:2])) * 60

def solution(m, musicinfos):
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a') # replace # notes

    duration = 0
    answer = ''
    for info in musicinfos:
        lst = info.split(',')
        lst[3] = lst[3].replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a') # replace # notes

        q, r = divmod(time_cal(lst[0], lst[1]), len(lst[3]))

        if m in lst[3] * q + lst[3][:r]:
            if time_cal(lst[0], lst[1]) > duration: # 조건을 일치하는 곡이 2곡 이상인 경우, 곡의 길이 확인 # 그렇지 않으면 무조건 먼저 들어온 곡을 정답으로
                duration = time_cal(lst[0], lst[1])
                answer = lst[2]

    if answer == '':
        return "(None)"
    else:
        return answer