import sys
sys.stdin = open("/Users/gibonghong/Downloads/input.txt", "r")

# # 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
#
# T = int(input())
#
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     tmp = input() # 숫자 버림
#     scores = {}
#
#     for i in input().split():
#         i = int(i)
#         if i in scores.keys():
#             scores[i] += 1
#         else:
#             scores[i] = 1
#
#     scores_desc = sorted(scores.items(), key=lambda x: (x[1], x[0]), reverse=True)
#     print('#{} {}'.format(test_case, scores_desc[0][0]))
#

# # 1859. 백만 장자 프로젝트
#
# T = int(input())
#
# # 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T+1):
#     _ = input()
#
#     income = 0
#     price_list = list(map(int, input().split()))
#
#     # 최고가의 인덱스로 경우의 수를 나눕니다.
#     while len(price_list) > 0:
#         idx = price_list.index(max(price_list)) # 최고가의 인덱스 반환
#         if idx == 0:
#             price_list.pop(0)
#         elif idx == len(price_list):
#             income += (price_list[idx]*(len(price_list)-1)) - sum(price_list[:-1])
#         else:
#             buy_list = price_list[:idx]
#             income += ((max(price_list)*len(buy_list)) - sum(buy_list))
#             price_list = price_list[idx+1:] # 최고가에 일단 다 판다
#
#     print('#{} {}'.format(test_case, income))

# # 1946. 간단한 압축 풀기
#
# T = int(input())
#
# for test_case in range(1, T+1):
#
#     # 한 줄에 모든 문자열 받기
#     mystr = ''
#     N = int(input())
#     for i in range(N):
#         pairs = input().split()
#         i = int(pairs[1])
#         mystr += pairs[0] * i
#
#     # 받은 문자열 조건에 맞게 정렬
#     answer = ''
#     i = 0
#     for s in mystr:
#         answer += s
#         i += 1
#         if i % 10 == 0:
#             answer += '\n'
#     print('#{}\n{}'.format(test_case, answer))

    # answer = ''
    #
    # N = int(input())
    # total = 0
    # for i in range(N):
    #     pairs = input().split()
    #     prev = total
    #     total += int(pairs[1])
    #     post = total
    #
    #     if total // 11 != 0:
    #         answer += pairs[0]*(10 - prev) + '\n' + pairs[0]*(post - 10)
    #         total = total % 10
    #         if total == 0:
    #             answer += '\n'
    #     else:
    #         answer += pairs[0]*int(pairs[1])
    #
    # print('#{} {}'.format(test_case, answer))


# 1979. 어디에 단어가 들어갈 수 있을까

# T = int(input())
#
# for test_case in range(1, T+1):
#     myarr = []
#     pair = list(map(int, input().split())) # pair = (5, 3)
#
#     # 행렬 형태의 list 생성
#     for i in range(pair[0]):
#         myarr.append(list(map(int, input().split())))
#
#     answer = 0
#     for line in myarr:
#         tmp = ''
#         for i in line:
#             tmp += str(i)
#         lst = tmp.split('0')
#         for item in lst:
#             if len(item) == pair[1]:
#                 answer += 1
#
#     # 행렬 transpose
#     myarr_T = list(zip(*myarr))
#     for line in myarr_T:
#         tmp = ''
#         for i in line:
#             tmp += str(i)
#         lst = tmp.split('0')
#         for item in lst:
#             if len(item) == pair[1]:
#                 answer += 1
#
#     print('#{} {}'.format(test_case, answer))

# # 2056. 연월일 달력
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     s = input()
#     year = s[0:4]
#
#     if s[4:6] in ['01', '03', '05', '07', '08', '10', '12']:
#         if int(s[6:]) in range(1, 32):
#             month = s[4:6]
#             date = s[6:]
#         else:
#             print('#{} {}'.format(test_case, -1))
#             continue
#     elif s[4:6] in ['04', '06', '09', '11']:
#         if int(s[6:]) in range(1, 31):
#             month = s[4:6]
#             date = s[6:]
#         else:
#             print('#{} {}'.format(test_case, -1))
#             continue
#     elif s[4:6] == '02':
#         if int(s[6:]) in range(1, 29):
#             month = s[4:6]
#             date = s[6:]
#         else:
#             print('#{} {}'.format(test_case, -1))
#             continue
#     else:
#         print('#{} {}'.format(test_case, -1))
#         continue
#
#     print('#{} {}/{}/{}'.format(test_case, year, month, date))

T = int(input())

# 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    _ = input()

    income = 0
    price_list = list(map(int, input().split()))

    while len(price_list) > 0:
        idx = price_list.index(max(price_list)) # 최고가의 인덱스 반환
        if idx == 0:
            price_list.pop(0)
        elif idx == len(price_list)-1:
            income += (price_list[idx]*(len(price_list)-1)) - sum(price_list[:-1])
            price_list = price_list[idx+1:]
        else:
            buy_list = price_list[:idx]
            income += ((max(price_list)*len(buy_list)) - sum(buy_list))
            price_list = price_list[idx+1:] # 최고가에 일단 다 판다

    print('#{} {}'.format(test_case, income))