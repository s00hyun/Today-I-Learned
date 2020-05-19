from itertools import permutations


def check(num, baseball):
    flag = 0
    for n, strike, ball in baseball:
        n = str(n)
        s_sum = 0
        b_sum = 0
        for i in range(3):
            if num[i] == n[i]:
                s_sum += 1
            elif num[i] in n:
                b_sum += 1
        if s_sum == strike and b_sum == ball:
            flag += 1
    if flag == len(baseball):
        # print(num, "is an answer")
        return 1
    else:
        return 0


def solution(baseball):
    answer = 0
    for num in permutations([str(i) for i in range(1, 10)], 3):
        num = ''.join(num)
        answer += check(num, baseball)

    return answer
