# 풀이 1 - Recursive
def pwrset(numbers: list, arr: list, idx: int, res: set):
    if idx == len(numbers):
        return

    for i in range(idx, len(numbers)):
        arr.append(numbers[i])
        if len(arr) < 2:
            pwrset(numbers, arr, i + 1, res)
        else:
            res.add(sum(arr))
        arr.pop()

    return res

def solution(numbers):
    res = list(pwrset(numbers, [], 0, set()))
    res.sort()
    return res

# ========================================================================
# # 풀이 2 - 이중 for문
# def solution(numbers):
#     answer = [numbers[i]+numbers[j] for i in range(len(numbers)) for j in range(i+1, len(numbers))]
#     answer = list(set(answer))
#     answer.sort()
#     return answer

