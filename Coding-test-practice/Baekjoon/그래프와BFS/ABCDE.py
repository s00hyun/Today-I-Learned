#-*- coding: utf-8 -*-

def answer():
    # n: 사람의 수 (정점의 수)
    # m: 친구 관계의 수 (간선의 수)
    n, m = map(int, input().split())

    # 인접행렬
    A = []
    # 인접리스트 (딕셔너리와 셋을 이용)
    A_list = {}
    # 간선리스트
    E_list = []

    for i in range(n):
        A.append([0] * n)
        A_list[i] = set()

    # 인접행렬, 인접리스트, 간선리스트 업데이트
    for i in range(m):
        n1, n2 = map(int, input().split())
        A[n1][n2] = 1
        A[n2][n1] = 1

        A_list[n1].add(n2)
        A_list[n2].add(n1)

        E_list.append([n1, n2])
        E_list.append([n2, n1])

    #print("인접행렬:\n", A)
    #print("인접리스트:\n", A_list)
    #print("간선리스트:\n", E_list)

    for e1 in E_list:
        for e2 in E_list:
            #print("e1:{}, e2:{}".format(e1, e2))

            # 서로 연결되어있지 않은 서로 다른 간선 2개 찾기 ( A(e1[0])->B(e1[1]), C(e2[0])->D(e2[1]) )
            if e1[0]==e2[0] or e1[1]==e2[1] or e2[1]==e1[0] or e1[1]==e2[0] or e1[0]==e1[1] or e2[0]==e2[1]:
                continue
            
            #print("A:{}, B:{}, C:{}, D:{}".format(e1[0], e1[1], e2[0], e2[1]))

            # B->C가 존재하는지 확인
            if A[e1[1]][e2[0]] != 1:
                continue
            
            # D->E 찾기
            if A_list[e2[1]] - set([e1[0], e1[1], e2[0], e2[1]]) != set():  # A,B,C,D가 아닌 정점이 존재
                return 1
            else:
                continue

    return 0

print(answer())