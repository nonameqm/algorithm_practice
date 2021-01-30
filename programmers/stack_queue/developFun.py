from collections import deque
import math
progresses=list(map(int, input().split()))
speeds=list(map(int, input().split()))


def solution(progresses, speeds):
    answer=[]
    complete=deque()
    for i in range(len(progresses)):
        complete.append(math.ceil((100-progresses[i])/speeds[i]))

    dist=complete.popleft()
    dist_num=1
    while len(complete)!=0:
        if dist>complete[0]:
            dist_num+=1
            complete.popleft()
        else:
            answer.append(dist_num)
            dist=complete.popleft()
            dist_num=1
    answer.append(dist_num)

    return answer

print(solution(progresses, speeds))