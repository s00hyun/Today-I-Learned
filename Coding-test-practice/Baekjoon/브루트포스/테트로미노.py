n, m = map(int, input().split())
arr = []
ans = 0
for i in range(n):
    arr.append( list(map(int, list(input().split()))) )


for i in range(n):
    for j in range(m-3):
        a = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3]
        if a > ans:
            ans = a

for i in range(n-3):
    for j in range(m):
        a = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]
        if a > ans:
            ans = a

for i in range(n-1):
    for j  in range(m-1):
        a = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]
        if a > ans:
            ans = a

for i in range(n-2):
    for j in range(m-1):
        a = []
        a.append(arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1])
        a.append(arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1])
        a.append(arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j])
        a.append(arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1])
        a.append(arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1])
        a.append(arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j])
        a.append(arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j])
        a.append(arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1])
        if max(a) > ans:
            ans = max(a)

for i in range(n-1):
    for j in range(m-2):
        a = []
        a.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j])
        a.append(arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2])
        a.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+2])
        a.append(arr[i][j+2] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2])
        a.append(arr[i][j+1] + arr[i][j+2] + arr[i+1][j] + arr[i+1][j+1])
        a.append(arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2])
        a.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1])
        a.append(arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2])
        if max(a) > ans:
            ans = max(a)

print(ans)