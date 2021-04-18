def movie_title(N:int):
    cnt, i = 0, 666
    while cnt != N:
        if '666' in str(i):
            cnt += 1
        i += 1
    return str(i-1)

print(movie_title(int(input())))
