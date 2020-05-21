def solution(prices):
    l = len(prices)
    check = [0] * l
    answer = [0] * l
    for i in range(l):
        for j in range(i + 1, l):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
            else:
                answer[i] = l - (i + 1)
    return answer

    return answer
