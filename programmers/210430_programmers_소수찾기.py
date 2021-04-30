from itertools import permutations

def solution(numbers):
    num_set = set()
    for i in range(1, len(numbers)+1):
        for n in list(map(''.join, permutations(numbers, i))):
            num_set.add(int(n))

    answer = 0
    for n in num_set:
        if n > 1:
            d = n - 1
            while d > 1:
                if n % d == 0:
                    break
                else:
                    d -= 1

            if d == 1:
                answer += 1

    return answer

print(solution(''))