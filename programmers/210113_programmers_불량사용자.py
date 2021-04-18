from collections import defaultdict
import itertools

def solution(user_id, banned_id):
    id_dict = defaultdict(list)
    for ban in set(banned_id): # banned_id element가 중복되는 경우를 고려해서 set()
        for user in user_id:
            # 두 문자열 비교하기
            if len(ban) == len(user):
                for idx in range(len(ban)):
                    if ban[idx] == '*': # banned_id 문자열에 *이 있으면 비교할 필요 없음
                        if idx == len(ban)-1:
                            id_dict[ban].append(user)
                        else:
                            continue
                    elif ban[idx] != user[idx]: # 문자열이 다르면 break
                        break
                    elif idx == len(ban)-1: # banned_id에 user_id가 해당하는 경우
                        id_dict[ban].append(user)

    mylist = [id_dict[id] for id in banned_id] # banned_id 각각이 매칭될 수 있는 user_id를 리스트에 받기

    # banned_id element를 기준으로 생성 가능한 모든 조합을 만들고, 순서에 따른 중복을 제거하여 결과 확인
    caselist = set(itertools.product(*mylist))
    answer = []
    for case in caselist:
        if len(set(case)) == len(banned_id):
            if set(case) not in answer:
                answer.append(set(case))

    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))

## 테스트케이스 5 시간초과
## 아마 permutation 때문일듯...
## 중복 피하는 법은 DFS로 구현해보기