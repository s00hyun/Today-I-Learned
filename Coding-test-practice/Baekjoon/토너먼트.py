n, a, b = map(int, input().split())

ans = 0
while True:
    if abs(a-b) == 1:
        if a%2 == 0:
            even = a
            odd = b
        else:
            even = b
            odd = a
        if even-odd > 0:  # a와 b가 같은 그룹에 배정됨 
            print(ans+1)
            break

    if a%2 == 0:  # 짝수
        a = a / 2
    else:
        a = a // 2 + 1
    if b%2 == 0:
        b = b / 2
    else:
        b = b // 2 + 1
    
    ans += 1
    