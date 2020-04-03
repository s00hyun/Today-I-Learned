from itertools import combinations


def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])
    col_list = [ [] for _ in range(col_len) ]
    #print("row_len: {}, col_len: {}, col_list: {}".format(row_len, col_len, col_list))
    col_idx = [i for i in range(col_len)]
    for rel in relation:
        for i in range(col_len):
            col_list[i].append(rel[i])
    #print(col_list)

    permu_list = []
    for i in range(1, col_len+1):
        permu_list += list(combinations(col_idx, i))
    #print("permu_list:", permu_list)

    superkey_list = []
    for iper in permu_list:
        temp_set = set()
        for j in range(row_len):
            temp = []
            for idx in iper:
                temp.append(relation[j][idx])
            temp_set.add(tuple(temp))
        if len(temp_set) == row_len:
            #print(temp_set)
            superkey_list.append(iper)
    #print("superkey_list:", superkey_list)

    slen = len(superkey_list)
    not_superkey = [0] * slen
    for i in range(slen):
        if not_superkey[i] == 1:
            continue
        s1 = superkey_list[i]
        for j in range(i+1, slen):
            if not_superkey[j] == 1:
                continue
            s2 = superkey_list[j]
            #print("s1: {}, s2: {}, set(s2) & set(s1): {}".format(s1, s2, set(s2) & set(s1)))
            if set(s2) & set(s1) == set(s1):
                not_superkey[j] = 1
                #print(s2, "is not superkey")
    #print("not_superkey:", not_superkey)

    return slen - sum(not_superkey)



print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
          ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
#print(solution([["a", "1", "4"], ["2", "1", "5"], ["a", "2", "4"]]))
