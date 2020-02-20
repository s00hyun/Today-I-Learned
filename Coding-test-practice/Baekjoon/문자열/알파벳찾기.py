string = input()
ans = [-1] * 26

for i in range(len(string)):
    index = ord(string[i]) - 97
    if ans[index] == -1:
        ans[index] = i

for a in ans:
    print(a, end=' ')
