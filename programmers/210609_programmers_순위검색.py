from collections import defaultdict

# def binary_search(arr: list, target: int) -> int:
#     if arr[len(arr) // 2] == target:
#         return
#
#     return

def solution(info: list, query: list) -> list:

    # define powerset function based on backtracking
    def powerset(arr: list, idx: int):
        for i in range(idx, 4):
            arr.append([0, 1, 2, 3][i])
            print(i, arr, idx)
            if i == 3:
                result.append(tuple(arr))
            else:
                powerset(arr, idx + 1)
            arr.pop()

    result = []
    powerset([], 0)
    print(result)

    dic = defaultdict(list)
    for s in info:
        s.split()
        for res in result:
            tmp = []
            for i in range(4):
                if i in res:
                    tmp.append('-')
                else:
                    tmp.append(s[i])

            dic[' and '.join(tmp)].append(s[-1])

    answer = []
    for q in query:
        q = q.split()
        q_new = ' '.join(q[:-1])
        v_list = dic[q_new]

        cnt = 0
        for v in v_list:
            if v >= q[-1]:
                cnt += 1
        answer.append(cnt)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
