t = int(input())

for i in range(t):
    # n = a1 + a2 + a3 + ... + a10 <= 10
    n = int(input())
    ans = 0

    # O( 3^(10) )
    for a1 in range(1, 3+1):
        if a1 == n:
            ans += 1
            break
        for a2 in range(1, 3+1):
            if a1 + a2 == n:
                ans += 1
                break
            for a3 in range(1, 3+1):
                if a1 + a2 + a3 == n:
                    ans += 1
                    break
                for a4 in range(1, 3+1):
                    if a1 + a2 + a3 + a4 == n:
                        ans += 1
                        break
                    for a5 in range(1, 3+1):
                        if a1 + a2 + a3 + a4 + a5 == n:
                            ans += 1
                            break
                        for a6 in range(1, 3+1):
                            if a1 + a2 + a3 + a4 + a5 + a6 == n:
                                ans += 1
                                break
                            for a7 in range(1, 3+1):
                                if a1 + a2 + a3 + a4 + a5 + a6 + a7 == n:
                                    ans += 1
                                    break
                                for a8 in range(1, 3+1):
                                    if a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 == n:
                                        ans += 1
                                        break
                                    for a9 in range(1, 3+1):
                                        if a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 == n:
                                            ans += 1
                                            break
                                        for a10 in range(1, 3+1):
                                            if a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 == n:
                                                ans += 1
                                                break

    print(ans)
