# brute-force로 풀면 시간 효율이 떨어짐... stack으로 풀기

def solution(prices):
    ans = [0]*len(prices) # prices 길이만큼의 정답 리스트 생성
    stack = [(0, prices[0])]
    for i, v in list(enumerate(prices[1:], start=1)):
        while True:
            if not stack or stack[-1][1] <= v:
                stack.append((i, v))
                break

            if stack[-1][1] > v:
                i_pop, v_pop = stack.pop()
                ans[i_pop] = i-i_pop

    while stack:
        i_pop, v_pop = stack.pop()
        ans[i_pop] = (len(prices)-1) - i_pop

    return ans

print(solution([1,2,3,2,3]))