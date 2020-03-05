"""
간단한 풀이:
0부터 n-1까지의 숫자에 대해, 숫자와 그 자릿수들의 합이 n과 같아질 때 그 숫자는 최소 생성자이다.
"""

n = input()
n = int(n)
ans = []

for i1 in range(10):
    for i2 in range(10):
        for i3 in range(10):
            for i4 in range(10):
                for i5 in range(10):
                    for i6 in range(10):
                        m = i1*100000 + i2*10000 + i3*1000 + i4*100 + i5*10 + i6
                        if m >= n:
                            break
                        if n - (i1+i2+i3+i4+i5+i6) == m:
                            ans.append(m)

#print(ans)
if len(ans) == 0:
    print(0)
else:
    print(min(ans))     
