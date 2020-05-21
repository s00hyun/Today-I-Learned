from collections import deque


# new code
def solution(priorities, location):
    pool = [(i, pri) for i, pri in enumerate(priorities)]
    q = deque(pool)
    answer = 0
    if len(priorities) == 1:
        return 1

    while True:
        maxp = max([x[1] for x in q])
        p = q.popleft()
        if p[1] < maxp:  # 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재함
            q.append(p)
            # print(q)
        else:
            answer += 1
            if p[0] == location:
                return answer


'''
def solution(priorities, location):
    c = 0
    index = deque()
    priorities = deque(priorities)
    for i in range(len(priorities)):
        index.append(i)
    
    while True:
        for i in range(len(priorities)):
            maximum = max(priorities)
            left_i = index.popleft()
            left = priorities.popleft()
            if left != maximum:
                index.append(left_i)
                priorities.append(left)
            else: 
                c += 1
                if left_i == location :
                    return c
'''


sol1 = solution([2,1,3,2], 2)
print(sol1)
sol2 = solution([1,1,9,1,1,1], 0)
print(sol2)
