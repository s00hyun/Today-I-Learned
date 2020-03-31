id_list = []
answer = set()


def go(idx, s, dst):
    if idx == dst:
        s = sorted(s)
        #print("add", s)
        answer.add(tuple(s))
        return
    for i in range(len(id_list[idx])):
        current_id = id_list[idx][i]
        if current_id not in s:
            s.append(current_id)
            go(idx + 1, s, dst)
            s.remove(current_id)


def solution(user_id, banned_id):
    for bid in banned_id:
        temp = []
        bid_len = len(bid)
        for uid in user_id:
            match = 1
            uid_len = len(uid)
            if bid_len != uid_len:
                continue
            for i in range(bid_len):
                if bid[i] == uid[i]:
                    continue
                elif bid[i] == '*':
                    continue
                else:
                    match = 0
                    break
            if match == 0:
                continue
            else:
                temp.append(uid)
        id_list.append(temp)
    #print(id_list)

    banned_id_len = len(banned_id)
    for i in range(len(id_list[0])):
        s = []
        s.append(id_list[0][i])
        go(1, s, banned_id_len)

    #print(answer)
    return len(answer)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
solution(user_id, banned_id)
