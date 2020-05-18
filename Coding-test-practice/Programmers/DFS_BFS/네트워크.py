# BOJ 섬의 갯수 문제와 **다르다!**

from collections import deque


visited = []


def bfs(i, n, comp):
    global visited
    q = deque()
    q.append(i)
    visited[i] = 1
    while q:
        v = q.popleft()
        for j in range(n):
            if comp[v][j] and not visited[j]:  # computer not visited
                visited[j] = 1  # visit
                q.append(j)
                #print("q:", q)
                #print("visited:", visited)
    #print("q:", q)
    #print("visit:", visited)
    return 1


def solution(n, computers):
    global visited
    visited = [0]*n
    answer = 0

    for i in range(n):
        if not visited[i]:
            #print("go", i)
            answer += bfs(i, n, computers)

    return answer


t1 = [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2]
t2 = [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1]
t3 = [5, [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]], 2]
t4 = [4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1], 1]]
#print(solution(t1[0], t1[1]))
#print(solution(t2[0], t2[1]))
#print(solution(t3[0], t3[1]))
print(solution(t4[0], t4[1]))

