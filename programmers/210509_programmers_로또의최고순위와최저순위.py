def solution(lottos, win_nums):
    cnt = len(set(win_nums) - set(lottos)) # 못 맞춘 개수
    low = 6 - cnt # 최소 정답 개수
    high = low + min(cnt, lottos.count(0))
    return [min(6, 7-high), min(6, 7-low)]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))