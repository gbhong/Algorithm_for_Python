# 정확성 풀이

from collections import deque

def solution(n, k, cmd):
    stack = deque()
    arr = [1 for _ in range(n)] # [1, 1, 0, 1, 1, 0, 1, 1]
    for c in cmd:
        if c[0] == 'U': # O(n)
            cnt = int(c.split()[-1])
            while cnt:
                k -= 1
                cnt -= arr[k] == 1

        elif c[0] == 'D': # O(n)
            cnt = int(c.split()[-1])
            while cnt:
                k += 1
                cnt -= arr[k] == 1

        elif c[0] == 'C': # O(n)
            arr[k] = 0
            stack.append(k)

            if sum(arr[k+1:]) == 0:
                while True:
                    k -= 1
                    if arr[k] == 1:
                        break
            else:
                while True:
                    k += 1
                    if arr[k] == 1:
                        break

        else:
            arr[stack.pop()] = 1

    return ''.join(['O' if i == 1 else 'X' for i in arr])


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
