a = [1,2,3]

for s in a:
    if s == 1:
        print(s, 'pass')
        pass
    elif s== 2:
        print(s, 'continue')
        continue
    else:
        print('else')
    print('continue면 이게 보이지 않아요')
