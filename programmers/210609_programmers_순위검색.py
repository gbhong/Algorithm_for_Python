

def solution(info, query):
    applicants = [s.split() for s in info]
    _query = [s.split(' and ') for s in query]

    return