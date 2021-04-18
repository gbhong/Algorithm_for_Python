def screening(gem_list:list, idx:int, prev:list):
    global gems
    gems_set = set()
    gems_set.add(gem_list[idx][1])

    for i, gem in gem_list[idx+1:]:
        gems_set.add(gem)
        print(i, gem)
        if len(gems_set) == len(set(gems)):
            result = [idx, i]
            if idx == 0:
                k = i - idx
                answer = result
            else:
                if result[1] - result[0] < answer[1] - answer[0]:
                    answer = result

    if result[1] - result[0] + 1 == len(set(gems)):
        return result
    else:
        idx += 1
        if idx == len(gem_list)-1:
            return answer
        else:
            return screening(gem_list, idx=idx, prev=answer)

def solution(gems):
    if len(set(gems)) == 1:
        return [1,1]

    else: # gems 집합의 원소가 2개 이상일 때
        gem_lst = list(enumerate(gems, 1))
        print(gem_lst)

        i=0; answer=[]
        screening(gem_lst, idx=i, prev=answer)

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))