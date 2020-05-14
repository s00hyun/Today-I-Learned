def solution(bridge_length, weight, truck_weights):
    truck_list = truck_weights[::-1]
    on_bridge = []
    check = []
    t = 0
    wsum = 0
    answer = 0

    while truck_list:
        for c in check:
            if c[1] >= bridge_length:
                on_bridge.remove(c[0])
                wsum -= c[0]
                c[1] = -1
            elif c[1] != -1:
                c[1] += 1

        if wsum < weight:
            if wsum + truck_list[-1] <= weight:
                truck = truck_list.pop()
                on_bridge.append(truck)
                wsum += truck
                answer = max(answer, t + bridge_length)
                check.append([truck,1])
        #print("t:", t, "on_bridge:", on_bridge)
        #print("check:", check)
        t += 1
    return answer + 1


bridge_length = [2, 100, 100]
weight = [10, 100, 100]
truck_weights = [[7,4,5,6], [10], [10,10,10,10,10,10,10,10,10,10]]
for i in range(3):
    print(solution(bridge_length[i], weight[i], truck_weights[i]))
    # 8, 101, 110
