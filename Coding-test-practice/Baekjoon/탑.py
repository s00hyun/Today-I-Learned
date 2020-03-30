import sys

n = int(sys.stdin.readline().rstrip())
height = list(map(int, sys.stdin.readline().rstrip().split()))

# 스택 이용 -> O(n)
stack = []
for i in range(n):
    h = height[i]
    while stack:
        num, top = stack[-1]
        if top >= h:
            print(num, end=' ')
            stack.append((i+1, h))
            break
        if top < h:
            stack.pop()
    if not stack:
        print(0, end=' ')
        stack.append((i+1, h))


'''
height = height[::-1]
ans = []

for i in range(n):
    if i == n - 1:
        ans.append(0)
        #print(ans)
        break
    for j in range(i+1, n):
        #print(height[i], "and", height[j])
        if height[i] <= height[j]:
            ans.append(n-j)
            #print(ans)
            break
        if j == n-1:
            ans.append(0)
            #print(ans)

ans = ans[::-1]
for a in ans:
    print(a, end=' ')
'''
