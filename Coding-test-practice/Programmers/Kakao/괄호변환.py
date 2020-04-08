# 문자열을 균형잡힌 문자열 u(최소),v로 분리
def split(string):
    stack = [string[0]]
    slen = len(string)
    for i in range(1, slen):
        s = string[i]
        if not stack:
            break
        else:
            upper = stack[-1]
            if upper == '(' and s == ')':
                stack.pop()
            elif upper == ')' and s == '(':
                stack.pop()
            else:
                stack.append(s)
    if i == slen - 1:
        u = string
        v = ''
    else:
        u = string[:i]
        v = string[i:]
    #print("u:", u, "v:", v)
    return u, v

#print(split(")("))
#print(split("()))((()"))
#print(split("))((()"))


# u가 올바른 괄호 문자열인지 체크
def check_ok(u):
    stack = []
    for s in u:
        if not stack:
            stack.append(s)
        else:
            upper = stack[-1]
            if upper == '(' and s == ')':
                stack.pop()
            else:
                stack.append(s)
        #print(stack)
    if stack:
        return False
    else:  # 스택이 모두 비었을 경우
        return True

#print(check_ok("(()))("))
#print(check_ok("(())()"))


def solution(p):
    result = ''
    if p == '':
        return ''

    # 문자열을 균형잡힌 문자열 u(최소),v로 분리 (스택 이용)
    u, v = split(p)

    if check_ok(u):  #u가 올바른 괄호 문자열
        return u + solution(v)
    else:  # u가 올바른 괄호 문자열이 아님
        result += '(' + solution(v) + ')'
        for s in u[1:-1]:
            if s == '(':
                result += ')'
            elif s == ')':
                result += '('
        return result

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))


