import re
from collections import defaultdict

def solution(str1, str2):
    pattern = re.compile('[a-zA-Z]{2}') # 영문자만 남기기
    cnt1, cnt2 = defaultdict(int), defaultdict(int) # dict for counting bigrams

    for c in range(0, len(str1) - 1):
        if pattern.match(str1[c:c + 2]):
            cnt1[str1[c:c + 2].lower()] += 1 # count

    for c in range(0, len(str2) - 1):
        if pattern.match(str2[c:c + 2]):
            cnt2[str2[c:c + 2].lower()] += 1 # count

    if len(cnt1.keys()) == 0 and len(cnt2.keys()) == 0: # return 1 when both are null
        return 65536
    else:
        numerator = set(cnt1.keys()) & set(cnt2.keys()) # 교집합
        denominator = set(cnt1.keys()) | set(cnt2.keys()) # 합집합

        numerator_lst, denominator_lst = [], []

        for token in numerator:
            k = min(cnt1[token], cnt2[token])
            numerator_lst.extend([token] * k) # 다중집합 생성

        for token in denominator:
            k = max(cnt1[token], cnt2[token])
            denominator_lst.extend([token] * k) # 다중집합 생성

        return int(len(numerator_lst) / len(denominator_lst) * 65536) # 정수부만 출력