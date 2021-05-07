# # 각 축(axis)에서 한 번 등장하는 좌표 리턴, Counter 활용
# from collections import Counter
#
# def solution(v):
#     x = Counter([p[0] for p in v]) # dict
#     y = Counter([p[1] for p in v])
#     return [Counter.most_common(x)[-1][0], Counter.most_common(y)[-1][0]]

# XOR 연산으로 풀이
def solution(v):
    answer = [0, 0]
    for x in [p[0] for p in v]:
        answer[0] ^= x
    for y in [p[1] for p in v]:
        answer[1] ^= y
    return answer

print(solution([[1,4],[3,4],[3,10]]))