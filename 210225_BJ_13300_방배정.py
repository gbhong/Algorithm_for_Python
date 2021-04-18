import sys
sys.stdin = open("/Users/gibonghong/Downloads/13300_input.txt", "r")

N, K = map(int, input().split()) # N은 학생 수, K는 한 방의 최대 인원 수

def make_dict(S:str, Y:str, mydict:dict):
    if Y+S not in mydict:
        mydict[Y+S] = 1
    else:
        mydict[Y+S] += 1

mydict = {}
for _ in range(N):
    S, Y = input().split() # S는 성별(0-여, 1-남), Y는 학년
    make_dict(S, Y, mydict)

answer = 0
for key in mydict:
    answer += (mydict[key]-1)//K + 1

print(answer)