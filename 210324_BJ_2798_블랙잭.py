N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

results = []
def pwrset(numbers, res, idx, M):
    global results
    '''
    ARGS:
        - numbers: (obj:list): given numbers
        - res: (obj:list): power set for each time step
        - idx: (obj:int): pointer
        - M: (obj:int): given upper bound for sum of power set

    :return: 부분집합 res의 합 중 M을 넘지 않는 최대수
    '''
    for i in range(idx, len(numbers)):
        res.append(numbers[i])

        if len(res) == 3: # 3개 다 뽑았는데 조건을 만족할 경우 그 합을 추가
            if sum(res) <= M:
                results.append(sum(res))
        else:
            pwrset(numbers, res, i+1, M)
        res.pop() # 3개 다 채웠는데 조건을 만족하지 못하면 다음 수를 넣기 위해 마지막 원소 제거

pwrset(numbers, [], 0, M)
results.sort()
print(results[-1])

## 결과 확인해보니 재귀보다 O(n^3)의 경우가 더 빨랐다...
## 재귀함수 잘못 구현했나??