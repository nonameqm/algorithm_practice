#문제 불완전

def find_firstzero(name):
    index=-1
    for i in range(len(name)):
       if ord(name[i])==65:
           index=i
    if index<=len(name)//2:
        return True
    else:
        return False


def solution(name):
    answer=0
    updown_list=[]
    for char in name:
        if ord(char)<77:
            updown_list.append(ord(char)-65)
        else:
            updown_list.append(91-ord(char))
    for number in updown_list:
        answer+=number
    answer+=(len(name)-1)

    return answer

print(solution('JAZ'))