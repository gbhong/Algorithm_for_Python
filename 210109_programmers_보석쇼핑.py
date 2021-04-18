def solution(gems):
    if len(set(gems)) == 1:
        return [1,1]

    else: # gems 집합이 2개 이상일 때
        gem_lst = list(enumerate(gems, 1))

        gems_set = set()
        gems_set.add(gem_lst[0][1])

        for i, gem in gem_lst[1:]:
            gems_set.add(gem)
            if len(gems_set) == len(set(gems)):
                answer = [1, i]
                break

        if answer[1] - answer[0] + 1 == len(set(gems)):
            return answer

        else:
            for i, gem in gem_lst[1:len(gems)-len(set(gems))+1]:
                gems_set = set()
                gems_set.add(gem)

                for j, gem_ in gem_lst[i:i+(answer[1]-answer[0])]:
                    gems_set.add(gem_)
                    if len(gems_set) == len(set(gems)):
                        break

                if len(gems_set) == len(set(gems)) and j-i < answer[1] - answer[0]:
                    answer = [i, j]

            return answer

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))