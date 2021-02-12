n=int(input())
lost=list(map(int, input().split()))
reserve=list(map(int, input().split()))


def solution(n, lost, reserve):
    answer = 0
    del_list=[]
    for item in lost:
        if item in reserve:
            del_list.append(item)

    for item in del_list:
        lost.remove(item)
        reserve.remove(item)

    for item in reserve:
        if item - 1 in lost:
            lost.remove(item - 1)
            continue
        if item + 1 in lost:
            lost.remove(item + 1)
            continue

    answer = n - len(lost)
    return answer

print(solution(n, lost, reserve))