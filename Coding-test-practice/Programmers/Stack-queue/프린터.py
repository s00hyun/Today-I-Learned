from collections import deque

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
                #print("max!")
                c += 1
                if left_i == location :
                    return c
            #print("priorities =", priorities)
            #print("index =", index)
            #print(c)

sol1 = solution([2,1,3,2], 2)
print(sol1)
sol2 = solution([1,1,9,1,1,1], 0)
print(sol2)
