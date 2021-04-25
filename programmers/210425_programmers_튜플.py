def solution(s):
    arr = s.lstrip('{').rstrip('}').split('},{')
    arr = [list(map(int, lst.split(','))) for lst in arr]
    arr.sort(key=lambda x: len(x))

    answer = arr[0]
    for idx in range(len(arr) - 1):
        n_set = set(arr[idx + 1]) - set(arr[idx])
        answer.append(list(n_set)[0])
    return answer