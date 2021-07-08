# define function for 'permutation with repetition', by using backtracking algorithm


def permutation_with_repeat(arr: list, depth: int, query: str):
    global letters, results, cnt

    if query in results: # check for duplication
        return

    if depth > 5: # 5 is the maximum length of result
        return

    if arr not in results and depth:
        results.append(arr)
        cnt += 1

    for i in range(5): # length of letters
        arr_ = arr
        arr_ += letters[i]
        permutation_with_repeat(arr_, depth + 1, query) # for loop continues after recursive call ends


letters = ['A', 'E', 'I', 'O', 'U']
results = []
cnt = 0

permutation_with_repeat('', 0, 'AAAE')
print(cnt)
