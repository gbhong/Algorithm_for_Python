import sys
sys.stdin = open("/Users/gibonghong/Downloads/6603_input.txt", "r")

while True:
    lst = input().split()
    k, S = lst[0], lst[1:]

    if k == '0': # 문제 조건
        break

    def pwrset(x: list, res:list, idx: int):
        '''
        :param x: 주어진 숫자 모음
        :param res: 부분집합
        :param idx: 원소를 담을 위치 인덱스
        :return:
        '''
        if idx == len(x): # 대상 리스트의 끝까지 가면 종료
            return

        for i in range(idx, len(x)):
            res.append(x[i]) # 선택지 택하기
            if len(res) == 6: # 6개 다 뽑으면 출력
                print(' '.join(res))
            else:
                pwrset(x, res, i+1) # 6개가 안 채워졌다면 다음 인덱스로 건너가기
            res.pop() # 다음 i가 올 수 있도록 방금 append 한 요소 제거

            '''
            pop()을 for문 제일 마지막에 넣음으로써 갈림길에서 다음 선택지를 택하는 코드 구현
            DFS, BFS랑은 조금 다른 개념 같음...
            '''

    pwrset(S, [], 0)
    print()

# def pwrset(res: list, idx: int):
#     global S
#     x = S[:]
#     if len(res) == 6:
#         print(' '.join(res))
#         return
#     else:
#         for i in range(idx, len(x)):
#             res.append(x[i])  # 선택지 택하기
#             pwrset(res, i + 1)  # 6개가 안 채워졌다면 다음 인덱스로 건너가기
#             res.pop()
#
# while True:
#     lst = input().split()
#     k, S = lst[0], lst[1:]
#
#     if k == '0': # 문제 조건
#         break
#      # 다음 i가 올 수 있도록 방금 append 한 요소 제거
#
#     pwrset([], 0)
#     print()