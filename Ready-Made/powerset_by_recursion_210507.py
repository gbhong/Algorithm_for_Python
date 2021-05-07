def powerset(arr:list, curr:list, idx:int):
    global res, M

    for i in range(idx, len(arr)):
        curr.append(arr[i])
        if len(curr) == M:
            res.append(tuple(curr))
        else:
            powerset(arr, curr, i+1)
        curr.pop()

res = []; M = 3
powerset([1,2,3,4,5], [], 0)
print(res)