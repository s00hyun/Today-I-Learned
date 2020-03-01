a, b = map(int, input().split())
arr = []

i = 1
while len(arr)<1000:
    arr = arr + [i] * i
    i += 1

#print(arr)
print(sum(arr[a-1:b]))