def solution(citations):
    citations = sorted(citations)
    clen = len(citations)
    for i in range(clen):
        if clen - i <= citations[i]:
            return clen - i
    return 0
    '''
    answer = 0
    for h in range(clen+1):  # h <= clen
        for i in range(clen):
            if citations[i] < h:
                continue
            if clen - i >= h:
                answer = max(answer, h)
    return answer
    '''
