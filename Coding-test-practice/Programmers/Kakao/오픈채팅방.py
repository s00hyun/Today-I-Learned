def solution(record):
    answer = []
    record_list = []
    for rec in record:
        record_list.append(rec.split())

    nick_dic = dict()
    for reclist in record_list:
        if reclist[0] == "Enter" or reclist[0] == "Change":
            nick_dic[reclist[1]] = reclist[2]
    for reclist in record_list:
        if reclist[0] == "Enter":
            answer.append(nick_dic[reclist[1]] + "님이 들어왔습니다.")
        elif reclist[0] == "Leave":
            answer.append(nick_dic[reclist[1]] + "님이 나갔습니다.")

    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
