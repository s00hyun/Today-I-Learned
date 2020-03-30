import sys

t = int(sys.stdin.readline().rstrip())


def go():
    n = int(sys.stdin.readline().rstrip())
    phone = [ sys.stdin.readline().rstrip() for _ in range(n) ]
    phone.sort()
    #print(phone)
    for i in range(n):
        for j in range(i+1, n):
            if phone[i] == phone[j][:len(phone[i])]:
                #print(phone[i], "and", phone[j][:len(phone[i])])
                return "NO"
    return "YES"


for _ in range(t):
    print(go())
