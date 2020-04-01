def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        #print("p:", participant[i], "c:", completion[i])
        if participant[i] != completion[i]:
            #print("here")
            return participant[i]

    return participant[-1]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))