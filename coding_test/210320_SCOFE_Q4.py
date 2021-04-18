score = list(map(float, input().split()))
score_map = dict()
for s in 'ABCDE':
    score_map[s] = score.pop(0)

# print(score_map)

N, M = map(int, input().split())

checklist = []
for i in range(N):
    contents = input()
    for j in range(M):
        checklist.append([contents[j],(i,j)])

genrelist = ''
for i in range(N):
    genrelist += input()

for j in range(N*M):
    checklist[j].append(genrelist[j])
    _ = score_map[genrelist[j]]
    checklist[j].append(_)

# print(checklist)

Y_lst, O_lst = [], []
for info in checklist:
    if info[0] == 'Y':
        Y_lst.append(info)
    elif info[0] == 'O':
        O_lst.append(info)

Y_lst.sort(key=lambda x: (x[3], -x[1][0], -x[1][1]), reverse=True)
for info in Y_lst:
    print(info[2], info[3], info[1][0], info[1][1])

O_lst.sort(key=lambda x: (x[3], -x[1][0], -x[1][1]), reverse=True)
for info in O_lst:
    print(info[2], info[3], info[1][0], info[1][1])