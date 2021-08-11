def solution(price, money, count):
    answer = 0
    s = 0
    
    for i in range (1, count+1):
        s += price*i

    if money < s:
        answer = abs(money-s)

    return answer
