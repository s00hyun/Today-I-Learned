from collections import deque


def solution(numbers, target):
    q = deque()
    q.append((0, 0, 0))
    length = len(numbers)
    answer = 0

    while q:
        n, op, idx = q.popleft()
        if idx == length and n == target:
            answer += 1
            continue
        if idx < length:
            q.append((n + (numbers[idx] * 1), 1, idx + 1))  # (숫자, +(1)/-(-1), 몇 번째인지)
            q.append((n + (numbers[idx] * (-1)), -1, idx + 1))

    return answer
