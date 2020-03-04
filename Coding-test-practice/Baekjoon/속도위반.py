"""
arr을 하나만 사용하는 방법:
1. arr = [0] * 100
2. 첫번째 루프: 범위 내 arr 요소에 각각 kmh만큼 빼주기
3. 두번째 루프: 범위 내 arr 요소에 각각 kmh만큼 더해주기
4. max(0, max(arr))
"""

n, m = map(int, input().split())
check = []
arr_n = []
arr_m = []
diff = []

km_ = 0
for i in range(n):
    km, kmh = map(int, input().split())
    #print("{} ~ {}, kmh={}".format(km_, km_+km, kmh))
    check.append(km)
    arr_n += [kmh] * (km_+km - km_)
    km_ += km
#print(arr_n)

km_ = 0
for j in range(m):
    km, kmh = map(int, input().split())
    #print("{} ~ {}, kmh={}".format(km_, km_+km, kmh))
    arr_m += [kmh] * (km_+km - km_)
    km_ += km
#print(arr_m)

c_ = 0
for i in range(n):
    c = c_ + check[i]
    temp = list(set(arr_m[c_:c]))
    for t in temp:
        if t >= arr_n[c-1]:
            diff.append(t - arr_n[c-1])
    c_ = c

#print(diff)
if len(diff) == 0:
    print(0)
else:
    print(max(diff))
