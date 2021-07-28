def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0
    
    while len(progresses) > 0:
        progress = progresses[0] + speeds[0] * day
        if progress >= 100: 
            progresses.remove(progresses[0])
            speeds.remove(speeds[0])
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
            day += 1
            count = 0
            
    print(count)
    answer.append(count)
    
    return answer
