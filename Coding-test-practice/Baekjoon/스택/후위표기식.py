import sys


expression = sys.stdin.readline().rstrip()
operator = []
operator_order = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2, ')': 2}
answer = ''

for e in expression:
    #print("*** for e =", e)
    if 'A' <= e <= 'Z':
        answer += e
    elif e in '+-*/':
        if not operator:
            operator.append(e)
        else:
            order_e = operator_order[e]
            order_top = operator_order[operator[-1]]
            if order_e > order_top:
                operator.append(e)
            elif order_e <= order_top:
                while operator and order_e <= operator_order[operator[-1]]:
                    if operator[-1] == '(':  # Runtime error without this condition
                        break
                    answer += operator.pop()
                operator.append(e)
    elif e == '(':
        operator.append(e)
    elif e == ')':
        while operator[-1] != '(':
            answer += operator.pop()
        operator.pop()  # Eliminate '(' from stack operator

    #print("  operator:", operator)
    #print("  answer:", answer)

while operator:
    answer += operator.pop()

print(answer)
