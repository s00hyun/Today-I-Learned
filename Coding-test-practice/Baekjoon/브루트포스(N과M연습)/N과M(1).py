# itertools를 이용하면 엄청 간단하게 찾을 수 있다

import itertools

n, m = map(int, input().split())

pool = [ str(i) for i in range(1, n+1) ]
ans = list( map(''.join, list(itertools.permutations(pool, m))) )
for a in ans:
    for i in range(m):
        print(a[i], end=' ')
    print()
    
"""
# 재귀함수 이용!ㅠㅠ

n, m = map(int, input().split())
c = [0] * 9  # 수열 생성 시 사용된 인덱스 저장
a = [0] * 9  # 각 반복에서 생성한 수열 저장

def go(index, n, m):
    global a
    #print("go({}, {}, {})".format(index, n, m))
    if index==m:
        for i in range(m):
            print(a[i], end=' ')
        print()
        a[index] = 0
        return 
    for i in range(1, n+1):  # 이번 인덱스에 사용될 숫자 고르기
        if c[i] == 1:  # 이미 사용한 숫자
            continue
        c[i] = 1
        a[index] = i
        go(index+1, n, m)  # 다음 인덱스에서부터 수열 생성&출력
        c[i] = 0
        

go(0, n, m)
"""