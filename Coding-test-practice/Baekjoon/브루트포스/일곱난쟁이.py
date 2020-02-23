import sys
h = []

for i in range(9):
    h.append(int(input()))

for i in range(9):
    for j in range(i+1, 9):
        if i==j:
            continue
        temp = [h[i], h[j]]
        ans = list(set(h) - set(temp))
        #print("ans:", ans)
        if sum(ans) == 100:
            ans.sort()
            for l in range(len(ans)):
                print(ans[l])
            sys.exit(0)
        