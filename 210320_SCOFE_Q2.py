# 점화식으로 접근

import time

def func(N:int, path:str):
    if path[-1] == '0': # 0에서는 다음 경로로 갈 수 없으므로 재귀호출 중단
        return 0
    else:
        # print(N, path, 'move on to the next one')
        return (func(N-1, path[:-1]) + func(N-2, path[:-2])) if N > 2 else 1

# 부분합의 개념으로 접근
def func2(N:int, path:str):
    if path[:3] == '101':
        a,b = 0,1
    elif path[:3] == '110':
        a,b = 1,0
    else:
        a,b = 1,2

    for idx in range(3, N):
        if path[idx] == '0':
            a, b = a, 0
        else:
            a, b = b, a+b

    return b

N = int(input())
path = input()
t1 = time.time()
print(func(N, path))
print(time.time()-t1)

t1p = time.time()
print(func(N, path))
print(time.time()-t1p)

# 경환 풀이

length = int(input())
road = input()

answer = 0
def check(now):
    global answer
    if now == len(road)-1:
        answer+=1
        # print(answer, 'road ENDS here')
        return
    else:
        if now+1 < len(road) and road[now+1]=='1':
            # print(now, '1 step')
            check(now+1)

        if now+2 < len(road) and road[now+2]=='1':
            # print(now, '2 step')
            check(now+2)
        return

t2 = time.time()
check(0) # 출발 지점부터 체크
print(answer)
print(time.time()-t2)