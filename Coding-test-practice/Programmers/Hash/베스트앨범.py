def solution(genres, plays):
    glen = len(genres)
    answer = []
    d = dict()
    dsum = dict()
    for i in range(glen):
        d[genres[i]].append((i, plays[i]))
        dsum[genres[i]] += plays[i]
    d_sort = sorted(dsum.items(), key=lambda x: x[1], reverse=True)
    for gen, total in d_sort:
        val = sorted(d[gen], key=lambda x: x[1], reverse=True)
        if len(val) == 1:
            answer.append(val[0][0])
        else:
            answer.extend([val[i][0] for i in range(2)])

    return answer
