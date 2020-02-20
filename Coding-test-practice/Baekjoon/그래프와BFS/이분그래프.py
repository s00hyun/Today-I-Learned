k = int(input())
answer = []

def result(v, e):
    g = [ [] for _ in range(v+1) ]
    edges = []
    check = [0] * (v+1)
    stack = []
    visited = set()
    color = 1
    for i in range(e):
        v1, v2 = map(int, input().split())
        if i==0:
            stack.append(v1)
        g[v1].append(v2)
        g[v2].append(v1)
        edges.append([v1, v2])
    print("graph:", g)
    print("edges:", edges)

    while stack:
        print("stack:", stack)
        vertex = stack.pop()
        if vertex not in visited:  
            visited.add(vertex)
            if check[vertex] == 0:
                check[vertex] = color
            stack.extend(g[vertex])
            #stack.extend(list(set(g[vertex]) - visited))
            for ver in list(set(g[vertex]) - visited):
                check[ver] = check[vertex] * -1
            
            print("vertex {} -> {}".format(vertex, check))

    for edge in edges:
        #print("{},{} = {},{}".format(edge[0], edge[1], check[edge[0]], check[edge[1]]))
        if (check[edge[0]] * check[edge[1]]) != -1:
            return "NO"
    return "YES"
        

for i in range(k):
    v, e = map(int, input().split())
    answer.append(result(v, e))

for ans in answer:
    print(ans)
