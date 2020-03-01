l = int(input())
string = input().replace(" ", "")
n = int(input())
comp = [ input().replace(" ", "") for _ in range(n) ]

ans = []

for i in range(l):
    s = string[i:] + string[:i]
    ans.append(s)
    
    s2 = ""
    for word in s:
        if word == '1':
            s2 += '3'
        elif word == '2':
            s2 += '4'
        elif word == '3':
            s2 += '1'
        elif word == '4':
            s2 += '2'
    #print("s2:", s2)
    ans.append(s2[::-1])

#print("comp:", comp)
#print("ans:", ans)

output = []
for c in comp:
    if c in ans:
        output.append(c)

#print("output:", output)
print(len(output))
for c in output:
    for i in range(l):
        print(c[i], end=' ')
    print()