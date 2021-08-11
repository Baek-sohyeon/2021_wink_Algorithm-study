def solution(array, commands):
    answer = []
    
    array = array[:]
    
    commands = commands[:]
    
    for list in commands:

        i = list[0]
        j = list[1]
        k = list[2]

        a = array[i-1:j]
        a.sort()
        b = a[k-1]
        answer.append(b)
        
    return answer
