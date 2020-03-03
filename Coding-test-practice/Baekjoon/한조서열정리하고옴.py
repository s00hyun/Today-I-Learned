n = int(input())
arr = list(map(int, input().split(' ')))
cnt = [0] * n


for i in range(n):
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            break
        if arr[j] < arr[i]:
            cnt[i] += 1

#print(cnt)
print(max(cnt))
        