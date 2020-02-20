n = int(input())
A = input().split(' ')
A = list(map(int, A))
A.sort()

m = int(input())
nums = input().split(' ')
nums = list(map(int, nums))

# minnum = min(A)
# maxnum = max(A)
ans = [0]
ans = ans * m

#print("A:", A)
#print("nums:", nums)

for i in range(m):
    # if nums[i] < minnum or nums[i] > maxnum:
    #     continue
    left = 0
    right = n-1

    #print("left:{} right:{} mid:{}".format(left, right, mid))

    while left <= right:
        mid = (left+right) // 2
        if A[mid] == nums[i]:
            ans[i] = 1
            #print("ans for {}: {}".format(i, ans))
            break
        if A[mid] < nums[i]:
            left = mid + 1
        else:
            right = mid - 1
    print(ans[i])