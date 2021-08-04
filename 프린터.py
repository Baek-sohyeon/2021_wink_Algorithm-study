# 참고 https://liveyourit.tistory.com/182

def solution(priorities, location):
    
    answer = 0
    
    while (len(priorities) > 0):

        if location == 0:
            if  priorities[0] < max(priorities) :
                priorities.append(priorities.pop(0))
                location = len(priorities) - 1
            else:
                answer +=1
                break;
        else: 
            if  priorities[0] < max(priorities) :
                priorities.append(priorities.pop(0))
                location -= 1

            else :
                priorities.pop(0)
                location -=1
                answer +=1

    return answer
