def sum_budgets(budgets, cutline):
    total = 0
    for b in budgets:
        if b <= cutline:
            total += b
        else:
            total += cutline
    return total


def solution(budgets, M):
    maximum = 0
    left = min(budgets)
    right = max(budgets)
    pivot = (left + right) // 2
    answer = sum_budgets(budgets, pivot)
    while left <= right:
        if answer > M:
            right = pivot - 1
            pivot = (left + right) // 2
            answer = sum_budgets(budgets, pivot)
            print("left:", left, "right:", right, "pivot:", pivot, "answer:", answer, "maximum:", maximum)
        elif answer < M:
            maximum = min(answer, M)
            left = pivot + 1
            pivot = (left + right) // 2
            answer = sum_budgets(budgets, pivot)
            print("left:", left, "right:", right, "pivot:", pivot, "answer:", answer, "maximum:", maximum)
    return pivot


print(solution([120, 110, 140, 150], 485))
