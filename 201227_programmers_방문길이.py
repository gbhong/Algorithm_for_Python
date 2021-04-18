def solution(dirs):
    dirs_dict = {'U': (0, 1),
                 'D': (0, -1),
                 'L': (-1, 0),
                 'R': (1, 0)
                 }

    visited = set() # 원점 출발
    prev = (0, 0) # 좌표 설정

    for d in dirs:
        if prev[0] == 5 and d == 'R':
            continue
        elif prev[0] == -5 and d == 'L':
            continue
        elif prev[1] == 5 and d == 'U':
            continue
        elif prev[1] == -5 and d == 'D':
            continue
        else:
            curr = tuple(map(sum, zip(prev, dirs_dict[d]))) # (0,1) + (1,0) = (1,1)
            visited.add(prev + curr) # prev-curr 경로를 저장 # (0,1) + (1,0) = (0,1,1,0)
            visited.add(curr + prev) # curr-prev 경로도 저장 # (1,0,0,1)
            prev = curr

    return len(visited)//2

print(solution('LULLLLLLU'))