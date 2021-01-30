from collections import deque
priorities=list(map(int, input().split()))
location=int(input())

def checkPriority(status, queue):
    for item in queue:
        if item[0]>status[0]:
            return False
    return True

def solution(priorities, location):
    answer=1
    target=[0 for i in range(len(priorities))]
    target[location]=1

    pqueue=deque(zip(priorities, target))

    while(True):
        #현재 대기열 앞줄 확인
        waitStatus=pqueue.popleft()
        #대기열 앞줄보다 우선 순위가 높은 것이 있다면 뒤로 마지막을 보냄
        if checkPriority(waitStatus, pqueue)==False:
            pqueue.append(waitStatus)
        #우선순위가 높은 것이 없다면
        else:
            #이 때 우리가 찾던 것이라면 break하고 return
            if(waitStatus[1]==1):
                break
            #아니라면 answer+1
            answer+=1
    return answer

print(solution(priorities, location))