# Hash & DFS
from collections import defaultdict


def solution(tickets):
    dic = defaultdict(list)
    for dept, dest in tickets:
        dic[dept].append(dest)
    for key in dic.keys():
        dic[key] = sorted(dic[key], reverse=True)  # 알파벳 역순으로 정렬

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in dic.keys() or not dic[top]:
            path.append(stack.pop())
        else:
            stack.append(dic[top].pop())

    return path[::-1]
