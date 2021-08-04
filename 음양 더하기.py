def solution(absolutes, signs):
    answer = 123456789
    
    absolutes = list(map(str,absolutes))
    signs = list(map(lambda x: '+' if x else '-', signs))
    lists = [*sum(zip(signs,absolutes),())]
    answer = eval(''.join(lists))
    return answer
