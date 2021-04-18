# def solution(n, times):
#     if n <= len(times):
#         return times[n-1]
#     else:
#         times_wait = [(i, i) for i in times] # (심사관마다 소요되는 시간, 대기 시간) 튜플 원소
#         n -= len(times)
#
#         while n>0:
#             times_wait = sorted(times_wait, key=lambda x: (x[0]+x[1]))
#             j = 1
#             while True:
#                 if times_wait[j] == times_wait[0]:
#                     j+=1
#                 else:
#                     break
#
#             for _ in range(min(n,j)):
#                 times_wait[:min(n,j)] = [(x, y+x) for (x, y) in times_wait[:min(n,j)]]
#
#             n -= min(n,j)
#
#         return sorted(times_wait, key=lambda x:x[1])[-1][-1]



print(solution(8, [4,7,10]))