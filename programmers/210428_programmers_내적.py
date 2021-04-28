def solution(a, b):
    return sum([i*j for i,j in zip(a,b)])

print(solution(a=[1,2,3,4], b=[-3,-1,0,2]))