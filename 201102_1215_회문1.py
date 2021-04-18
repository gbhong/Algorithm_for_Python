import sys
sys.stdin = open("/Users/gibonghong/Downloads/input.txt", "r")

# 1215. [S/W 문제해결 기본] 3일차 - 회문1
def palindrome(line, window_size): # line별로 회문 찾는 함수 생성
    cnt = 0
    for i in range(8 - window_size + 1):
        if line[i:i+window_size] == line[i+window_size-1::-1][:window_size]:
            cnt += 1
    return cnt

for test_case in range(1, 11): # 10개의 테스트 케이스에 대해 8*8 글자판 만들기
    window_size = int(input())
    arr = []
    for i in range(8):
        arr.append(input())
    arr_T = list(zip(*arr))

    ans = 0
    for i in range(8):
        ans += palindrome(arr[i], window_size) + palindrome(arr_T[i], window_size)

    print('#{} {}'.format(test_case, ans))