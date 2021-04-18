# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = input()

cnt, answer = 0, 0 # 사용자 수와 정답 할당
low, high = 0, 2400 # 모두가 가능한 시간 설정

while cnt < int(N):
    t1, _, t2 = input().split() # t1은 t2보다 빠른 시간
    t1 = int(t1.replace(':',''))
    t2 = int(t2.replace(':',''))

    if t2 <= low or t1 >= high: # 현재 사용자의 시간이 기존 구간과 겹치지 않는 경우, 모두가 가능한 시간은 없다
        answer = '-1'
        break
    else:
        low = max(t1, low)
        high = min(t2, high)

    cnt += 1

if cnt < int(N):
    print(answer)
else:
    low, high = str(low), str(high)
    while len(str(low)) < 4:
        low = '0' + low
    while len(str(high)) < 4:
        high = '0' + high

    print(f'{low[0:2]}:{low[2:]} ~ {high[0:2]}:{high[2:]}')
