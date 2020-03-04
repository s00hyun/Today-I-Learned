s = list(input())
dic = {}
ans = 0

for a in ['A','B','C']:
    dic[a] = 2
for a in ['D','E','F']:
    dic[a] = 3
for a in ['G','H','I']:
    dic[a] = 4
for a in ['J','K','L']:
    dic[a] = 5
for a in ['M','N','O']:
    dic[a] = 6
for a in ['P','Q','R','S']:
    dic[a] = 7
for a in ['T','U','V']:
    dic[a] = 8
for a in ['W','X','Y','Z']:
    dic[a] = 9

for a in s:
    ans += dic[a]+1
print(ans)
