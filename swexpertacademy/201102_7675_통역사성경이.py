import sys
sys.stdin = open("/Users/gibonghong/Downloads/s_input.txt", "r")

# 7675. 통역사 성경이
T = int(input())
for test_case in range(1, T+1):
    _ = int(input())
    lst = input().replace('!', '.').replace('?','.')
    lst = lst.split('.')[:-1]
    print(lst)

    result = []
    for sentence in lst:
        names = [name for name in list(filter(lambda x: x[0].isupper(), sentence.split()))]
        names = [name for name in names if all(char.islower() for char in name[1:])]
        result.append(str(len(names)))
    answer = ' '.join(result)

    print('#{} {}'.format(test_case, answer))