from itertools import permutations


def check(num):
    if num == 0 or num == 1:
        return 0
    for i in range(2, num):  # [2, num-1]
        if num % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    result = set()
    for i in range(1, len(numbers)+1):
        for item in permutations(numbers, i):
            result.add(int(''.join(item)))
    result = list(set(result))
    #print(result)
    for num in result:
        answer += check(num)
    return answer
