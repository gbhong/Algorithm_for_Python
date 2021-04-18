import sys
sys.stdin = open("/Users/gibonghong/Downloads/input.txt", "r")

# Assign test cases
for tc in range(1, 11):
    _ = input()

    # 주어진 100*100 2차원 평면에 맞는 인접행렬 생성
    adj_matrix = [input().split() for _ in range(100)]

    answer = (99, 99999)
    # 일단 왼쪽이나 오른쪽으로 가고, 불가능한 경우 아래로 내려가는 코드
    for j in range(99, -1, -1): # 복수 개인 경우 가장 큰 x 좌표를 반환
        if adj_matrix[0][j] == '1':
            curr = j
            visited = [[0] * 100 for _ in range(100)]
            visited[0][curr] = 1

            i = 0
            while i < 99: # 사다리가 내려지는 순간 무조건 끝까지 내려갈 수 있음
                # print(i, j)
                if (0 <= curr-1) and (adj_matrix[i][curr-1] == '1') and not visited[i][curr-1]: # to the left
                    visited[i][curr - 1] = visited[i][curr] + 1
                    curr -= 1
                elif (curr+1 < 100) and (adj_matrix[i][curr+1] == '1') and not visited[i][curr+1]: # to the right
                    visited[i][curr + 1] = visited[i][curr] + 1
                    curr += 1
                else: # to downward, never be visited
                    visited[i+1][curr] = visited[i][curr] + 1
                    i += 1

            if visited[99][curr] < answer[1]:
                answer = (j, visited[99][curr])

    print(f'#{tc} {answer[0]}')