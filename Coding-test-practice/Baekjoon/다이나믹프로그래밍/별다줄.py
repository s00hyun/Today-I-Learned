# 런타임 에러
# 재귀로 풀기에는 단어 길이가 길어서 DP로 풀어야 할 것 같다.

import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
words = [ sys.stdin.readline().rstrip() for _ in range(N) ]
target = sys.stdin.readline().rstrip()
target_len = len(target)
answer = 0
modnum = 10**9 + 7

word_dic = defaultdict(int)
for word in words:
    for i in range(len(word)):
        w = word[:i+1]
        word_dic[w] += 1
key_list = list(word_dic.keys())
#print(word_dic)
#print(key_list)


def go(index, length, ans):
    global answer
    if index > length:
        #print("Already done")
        return
    elif index == length:
        answer += ans
        answer %= modnum
        #print("ans:", ans)
        return

    k = target[index]  # 'a'
    for key in key_list:
        if k not in key:  # 'a'(k) in 'aa'(key)
            continue
        if target[index:index+len(key)] != key:
            #print("target:", target[index:index+len(key)] , ". Does not match")
            continue
        #print(key, "go({}, {}, {})".format(index+len(key), length, ans*word_dic[key]))
        go(index+len(key), length, (ans*word_dic[key]) % modnum)


#print("go({}, {}, {})".format(0, target_len, 1))
go(0, target_len, 1)
print(answer)
