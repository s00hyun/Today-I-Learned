# 실패


def solution(stones, k):
    # 돌다리를 건널 수 있는 놈들의 최댓값(m)을 이분탐색으로 찍는다
    left = 0
    right = max(stones)
    while left <= right:
        max_0 = 0
        temp = []
        m = (left + right) // 2
        for s in stones:
            temp.append(max(0, s - (m - 1)))
        print("m:", m, "temp:", temp)
        for i in range(len(temp) - k):
            cnt = temp[i:i+3].count(0)
            max_0 = max(max_0, cnt)
            print("cnt:", cnt, "max_0:", max_0)
        if max_0 < k:
            left = m + 1
        elif max_0 > k:
            right = m - 1
        else:
            return m - 1
    return m - 1


print(solution([2, 3, 1, 4, 6], 1))
