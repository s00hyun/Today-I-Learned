import sys
from collections import deque


# t1 < t2 => return 1
# t1 > t2 => return 0
def smaller(t1, t2):
    t1_a, t1_n = t1
    t2_a, t2_n = t2
    if t1_a < t2_a:
        return 1
    elif t1_a > t2_a:
        return 0
    else:  # t1_a == t2_a
        if t1_n < t2_n:
            return 1
        else:
            return 0


def make_line(s, q):
    line = []

    while q:
        if not s:
            s.append(q.popleft())
        if not q:
            break
        s_top = s[-1]
        q_head = q[0]
        q_next = None
        if len(q) > 1:
            q_next = q[1]

        if smaller(q_head, s_top):
            if not q_next:
                line.append(q.popleft())
                continue
            if not smaller(q_head, q_next):
                s.append(q.popleft())
            else:
                line.append(q.popleft())

        else:  # q_head > s_top
            #print("q_head: {} < s_top: {} ==> s.pop()".format(s_top, q_head))
            line.append(s.pop())

        #print("----------")
        #print(s)
        #print(q)
        #print("line:", line)


    #print(s)
    #print(q)

    if s:
        line.extend(reversed(s))

    #print("line: {}, sorted line:{}".format(line, sorted(line)))
    if line == sorted(line):
        return "GOOD"
    else:
        return "BAD"


n = int(sys.stdin.readline().rstrip())
tickets = []
for _ in range(n):
    tickets.extend(list(sys.stdin.readline().rstrip().split()))
stack = []
queue = deque()
for ticket in tickets:
    t_a, t_n = ticket.split('-')
    queue.append((t_a, int(t_n)))

print(make_line(stack, queue))
