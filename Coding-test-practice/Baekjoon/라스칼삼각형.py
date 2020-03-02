""" 
RecursionError: maximum recursion depth exceeded in comparison

def R(n, m):
    if m == 0:
        return 1
    if n == m:
        return 1
    if m == 1 or m == n-1:
        return n

    #print("(R({}, {}) * R({}, {}) + 1) // R({}, {})".format(n-1, m-1, n-1, m, n-2, m-1))
    return (R(n-1, m-1) * R(n-1, m) + 1) // R(n-2, m-1)
"""


cases = int(input())

for i in range(cases):
    n, m = map(int, input().split())
    #print(R(n, m))
    print((n-m) * m + 1)