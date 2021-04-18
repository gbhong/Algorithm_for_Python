def solution(n, works):
    if n >= sum(works):
        return 0
    else:
        while n > 0:
            works.sort() # max 계산과 slicing을 편하게 하기 위해
            k = works.count(works[-1]) # maximum value의 개수 구하기
            works[-1:-1-min(n,k):-1] = [i-1 for i in works[-1:-1-min(n,k):-1]] # slicing, n과 k 중 작은 값만큼 1씩 뺴준다
            n -= min(n,k)

        return sum([x*x for x in works])

print(solution(4, [4,3,3]))


a = [1,2,3,4,5]