import sys
sys.stdin = open("/Users/gibonghong/Downloads/13300_input.txt", "r")

N, K = map(int, input().split()) # N은 학생 수, K는 한 방의 최대 인원 수

mylst = []; rooms = 0
for _ in range(N):
    student = ''.join(input().split()) # S는 성별(0-여, 1-남), Y는 학년
    if student not in mylst:
        mylst.append(student)
        rooms += 1
    elif mylst.count(student) == K:
        mylst = [s for s in mylst if s != student]
        rooms += 1
    else:
        mylst.append(student)

print(rooms)