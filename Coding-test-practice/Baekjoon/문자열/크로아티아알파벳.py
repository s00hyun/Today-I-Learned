cro = { 'c': ['c=', 'c-'], 'd': ['dz=', 'd-'], 
       'l': ['lj'], 'n': ['nj'], 's': ['s='], 'z': ['z='] }

s = input()
ans = 0

i = 0
while i < len(s):
    #print("i:", i)
    if s[i] in cro.keys():
        if s[i:i+2] in cro[s[i]]:
            #print(s[i:i+2])
            i += 2
            ans += 1
        elif s[i:i+3] in cro[s[i]]:  # 'dz='
            #print(s[i:i+3])
            i += 3
            ans += 1
        else:
            #print(s[i])
            i += 1
            ans += 1
    else:
        #print(s[i])
        i += 1
        ans += 1

print(ans)


"""
cro = ['c=','dz=','nj','c-','z=','d-','lj','s=']
S = input()
for c in cro:
    S = S.replace(c,'*')
print(len(S))
"""