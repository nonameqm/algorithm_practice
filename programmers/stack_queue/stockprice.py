def solution(prices):
    answer=[]
    for i in range(len(prices)):
        time=0
        for j in range(i, len(prices)):
            if prices[j]<prices[i] or j==len(prices)-1:
                answer.append(time)
                break
            else:
                time+=1
    return answer

prices=list(map(int, input().split()))
print(prices)
print(solution(prices))