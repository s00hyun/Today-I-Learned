# 실패 (66.0 / 100.0)
# 2, 6, 11, 12, 14, 15, 17, 26, 27, 28


def solution(s):
    answer = 1001
    slen = len(s)
    result = set()

    sliced_list = []
    for i in range(1, slen + 1): #(slen // 2) + 2):  # 자를 길이
        temp = []
        for j in range(0, slen // i):
            if j == (slen // i) - 1:
                temp.append(s[i*j :])
            else:
                temp.append(s[i*j : i*(j+1)])
        temp.append('0')
        print(temp)
        sliced_list.append(temp)

    for slist in sliced_list:
        temp_s = ''
        si = 0
        for i in range(len(slist)):
            ei = i
            if slist[si] != slist[ei]:
                if ei - si > 1:
                    temp_s += (str(ei - si) + slist[si])
                else:
                    temp_s += slist[si]
                si = ei

        result.add(temp_s)

    print(result)
    for res in result:
        answer = min(answer, len(res))

    return answer


print(solution(str('a'*5)))
#print(solution(str('a'*10)))  # 3
#print(solution(str('a'*100)))  # 4
#print(solution(str('a'*1000)))  # 5

print(solution("a"))
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))