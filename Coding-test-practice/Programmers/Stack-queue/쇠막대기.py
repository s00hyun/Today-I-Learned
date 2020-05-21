def solution(arrangement):
    arrangement = arrangement.replace("()", 'L')
    #print(arrangement)
    stick = 0
    answer = 0
    stack = []
    for i, a in enumerate(arrangement):
        if a == '(':
            stick += 1
            stack.append(a)
        elif a == ')':
            stick -= 1
            answer += 1
            stack.pop()
        elif a == 'L':
            answer += stick
            #print(answer)
    return answer


print(solution("()(((()())(())()))(())"))  # 17
