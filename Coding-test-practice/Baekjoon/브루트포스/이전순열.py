import sys

n = int(sys.stdin.readline().rstrip())
permu = list(map(int, sys.stdin.readline().rstrip().split()))


def next_permutation(_permu):
    if n == 1:
        print(-1)
        return

    i = n-1
    while _permu[i-1] <= _permu[i]:  # 순열의 끝에서부터 탐색: 오름차순 순열이 시작되기 직전의 index 찾기 (i-1)
        i -= 1
    #print(i-1)
    if i-1 < 0:
        print(-1)
        return

    j = n-1
    while _permu[i-1] <= _permu[j]:  # 순열의 끝에서부터 탐색:_permu[i-1]보다 작거나 같은 숫자를 만나면 종료 (index: j)
            j -= 1
    #print(i-1, j)

    # _permu[i-1]와 _permu[j]를 swap
    temp = _permu[i-1]
    _permu[i-1] = _permu[j]
    _permu[j] = temp

    # permu[i:]를 뒤집음
    p = _permu[i:]
    p.reverse()
    _permu[i:] = p
    #print(_permu)

    for num in _permu:
        print(num, end=' ')
    return


next_permutation(permu)
