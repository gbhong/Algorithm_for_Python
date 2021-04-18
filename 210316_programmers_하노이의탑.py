class hanoi(object):
    def __init__(self):
        self.answer = [] # 빈 리스트 생성

    def towers(self, n:int, source:int, dest:int, aux:int):
        if n == 1:
            self.answer.append([source, dest])
        else:
            self.towers(n-1, source=source, dest=aux, aux=dest) # M(n-1)
            self.answer.append([source, dest]) # 마지막 원판을 dest로 옮겨주기
            self.towers(n-1, source=aux, dest=dest, aux=source) # M(n-1)

    def solution(self, n:int):
        self.towers(n, source=1, dest=3, aux=2) # 1번 탑에서 3번 탑으로 옮기는 task
        return self.answer

hanoi = hanoi()
print(hanoi.solution(3))

# def towers(n:int, source:int, dest:int, aux:int, answer:list):
#     if n == 1:
#         answer.append([source, dest])
#     else:
#         towers(n-1, source=source, dest=aux, aux=dest, answer=answer) # M(n-1)
#         answer.append([source, dest]) # 마지막 원판을 dest로 옮겨주기
#         towers(n-1, source=aux, dest=dest, aux=source, answer=answer) # M(n-1)
#
# def solution(n:int):
#     answer = []
#     towers(n, source=1, dest=3, aux=2, answer=answer) # 1번 탑에서 3번 탑으로 옮기는 task
#     return answer
#
# print(solution(3))