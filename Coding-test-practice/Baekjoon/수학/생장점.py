import sys

while True:
    arr = list(map(int, sys.stdin.readline().split(' ')))
    #print(arr)
    year = arr[0]
    if year == 0:
        break

    result = 1
    for i in range(1, year+1):
        s = arr[2*i - 1]
        t = arr[2*i]
        result *= s
        result -= t

    print(result)
