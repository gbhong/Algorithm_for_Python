def solution(n, results):
    win_dict, lose_dict = {}, {}
    ans = 0

    for i in range(1, n + 1):
        win_dict[i] = set()
        lose_dict[i] = set()

    for res in results:  # 이긴 그래프와 진 그래프 만들기
        win_dict[res[0]].add(res[1])
        lose_dict[res[1]].add(res[0])

    for i in range(1, n + 1):  # 전적 업데이트하기
        for loser in win_dict[i]:
            lose_dict[loser].update(lose_dict[i])
        for winner in lose_dict[i]:
            win_dict[winner].update(win_dict[i])

    for i in range(1, n + 1):
        if len(win_dict[i]) + len(lose_dict[i]) == n - 1:
            ans += 1

    return ans


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])

# DFS로 풀어보기