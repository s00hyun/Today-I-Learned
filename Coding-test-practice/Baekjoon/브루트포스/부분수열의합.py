n, s = map(int, input().split())
seq = list(map(int, input().split()))
l = len(seq)
ans = 0

def go(index, sum):
    global ans
    #print("go({}, {})".format(index, sum))
    if index == n-1:
        if sum == s:
            ans += 1
            #print("ans=", ans)
        return

    go(index+1, sum+seq[index+1])  # 수열의 다음 원소를 선택할 경우
    go(index+1, sum)  # 수열의 다음 원소를 선택하지 않을 경우


go(-1, 0)

# 합이 0인 부분수열을 찾을 경우, 아무것도 선택하지 않는 경우(공집합)도 카운트되므로 1을 빼 준다.
if s == 0:  
    ans -= 1

print(ans)
      