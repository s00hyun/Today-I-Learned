import sys

n = int(sys.stdin.readline().rstrip())
mix = list(map(int, sys.stdin.readline().split()))
cards = [i for i in range(1, n+1)]
length = [0] * n
answer = 1


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


for i in range(n):
    #print("** curr:", cards[i])
    if length[i]:
        continue
    start = cards[i]
    curr = cards[i]
    l = 0
    temp = []
    if start == mix[i]:
        length[i] = 1
        continue
    while True:
        next = mix[curr-1]
        curr = next
        l += 1
        temp.append(next)
        #print("next:", next)
        if curr == start:
            for t in temp:
                length[t-1] = l
            #print("length:", l)
            break
    answer = lcm(answer, l)

#print(length)
print(answer)
