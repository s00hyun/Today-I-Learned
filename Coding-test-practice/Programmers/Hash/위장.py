from collections import defaultdict


def solution(clothes):
    answer = 1
    cdict = defaultdict(int)
    for cname, ctype in clothes:
        cdict[ctype] += 1  # 각 의상의 종류를 선택하지 않는 경우를 추가
    clist = [num + 1 for num in cdict.values()]

    for n in clist:
        answer *= n

    return answer - 1  # 아무 의상도 선택하지 않는 경우도 포함되므로 1을 뺀다
