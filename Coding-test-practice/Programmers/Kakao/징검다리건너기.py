def solution(stones, k):
    # 돌다리를 건널 수 있는 놈들의 최댓값(m)을 이분탐색으로 찍는다
    left = 0
    right = 200000000
    max_0 = 0
    while left < right:
        print("left:{}, right:{}".format(left, right))
        m = (left + right) // 2
        cnt = 0
        fl=0

        print("m:", m)
        for i in range(len(stones)):
            if stones[i] - m <= 0:
                cnt += 1
                if cnt >= k:
                    fl=1
                    print("cnt1:", cnt)
                    right = m
                    break
            else:
                cnt = 0
        if fl==0:
            print("cnt2:", cnt)
            max_0 = max(max_0, m+1)
            print("max_0:", max_0)
            left = m + 1

    return max_0

#print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
#print(solution([2, 3, 1, 4, 6], 1))
print(solution([3,3,3,3], 1))