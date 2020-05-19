from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    words.insert(0, begin)
    wlen = len(words)
    l = len(words)
    g = [[0] * wlen for _ in range(wlen)]
    target_idx = words.index(target)
    #print("words:", words)
    #print("target_idx:", target_idx)

    for i in range(wlen):
        for j in range(i + 1, wlen):
            #print(words[i], "and", words[j])
            wcount = 0
            for w1, w2 in zip(list(words[i]), list(words[j])):
                if w1 != w2:
                    wcount += 1
            #print("wcount:", wcount)
            if wcount == 1:
                g[i][j] = 1
                g[j][i] = 1
    #print("g:", g)

    q = deque()
    check = [-1] * wlen
    q.append(0)
    check[0] = 0

    while q:
        #print("q:",q)
        #print("check:",check)
        v = q.popleft()
        for i in range(wlen):
            nv = g[v][i]
            # print("nv:", nv, "check[nv]:", check[nv])
            if nv and check[i] == -1:
                # print("check", nv)
                check[i] = check[v] + 1
                q.append(i)

    return check[target_idx]


#print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
#print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
print(solution("hit", "hhh", ["hhh", "hht"]))  # 2
