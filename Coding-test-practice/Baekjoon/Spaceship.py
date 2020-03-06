import sys

n = int(sys.stdin.readline())
arr = list(map(int, list(sys.stdin.readline().split())))

last = 0
s = sum(arr)
for i in range(n):
    last = arr[i]
    if s - last == last:
        arr.remove(arr[i])
        break

for i in range(n-1):
    print(arr[i], end=' ')
print(last)