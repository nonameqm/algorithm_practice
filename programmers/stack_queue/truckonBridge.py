from collections import deque
bridge_length=int(input())
weight=int(input())
truck_weights=list(map(int, input().split()))

def sum(truck_on_bridge):
    sum=0
    for item in truck_on_bridge:
        sum+=item[0]
    return sum


def solution(bridge_length, weight, truck_weights):
    answer=0
    truck_on_bridge=[]
    departure_time=1
    while len(truck_weights)!=0:
        if sum(truck_on_bridge)+truck_weights[0] > weight:
            if truck_on_bridge[len(truck_on_bridge)-1][1]>=truck_on_bridge[0][1]+bridge_length:
                pass
            else:
                departure_time = truck_on_bridge[0][1] + bridge_length
            truck_on_bridge.pop(0)
        else:
            truck = truck_weights.pop(0)
            truck_on_bridge.append([truck, departure_time])
            departure_time += 1

        print(truck_on_bridge, ' : ', truck_weights)

    answer=truck_on_bridge[len(truck_on_bridge)-1][1]+bridge_length
    return answer

print(solution(bridge_length, weight, truck_weights))