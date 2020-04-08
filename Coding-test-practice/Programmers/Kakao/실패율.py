def solution(N, stages):
    result = []
    nonclear = [0] * (N + 2)
    on_pass_stage = [0] * (N + 2)

    for s in stages:
        nonclear[s] += 1
        for i in range(1, s + 1):
            on_pass_stage[i] += 1
    # print(nonclear)
    # print(on_pass_stage)

    i = 1
    for nc, op in zip(nonclear[1:N + 1], on_pass_stage[1:N + 1]):
        if op == 0:
            result.append((i, 0))
        else:
            result.append((i, nc / op))
        i += 1
    # print(result)

    result.sort(key=lambda x: x[1], reverse=True)
    answer = [res[0] for res in result]

    return answer
