import math


def solution(progresses, speeds):
    day = []
    stack = []
    answer = []
    l = len(progresses)
    for i in range(l):
        result = math.ceil((100 - progresses[i]) / speeds[i])
        day.append(result)
    # print(day)

    for d in day:
        if not stack:
            stack.append(d)
            answer.append(1)
        elif stack[0] >= d:
            stack.append(d)
            answer[-1] += 1
        else:  # stack[0] < d
            stack = [d]
            answer.append(1)

    return answer