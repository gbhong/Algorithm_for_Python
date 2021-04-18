import sys
sys.stdin = open("/Users/gibonghong/Downloads/sample_input.txt", "r")

# 5642. 합
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    curr = arr[0]; res = [curr]

    for i in range(1, N):
        if curr >= 0:
            if arr[i] < 0:
                res.append(curr)
            curr += arr[i]
        else:
            if arr[i] < 0:
                res.append(curr)
            curr = arr[i]

    res.append(curr) # 마지막 최종 합은 더해준다

    print('#{} {}'.format(test_case, max(res)))