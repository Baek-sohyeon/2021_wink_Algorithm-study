def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)

    for i in range(len(citations)):
        if citations[i] > i:
            answer += 1


    return answer
