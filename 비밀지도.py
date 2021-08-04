def solution(n, arr1, arr2):
    answer = []
    arr1 = (list(map(lambda x:format(x,'b'),arr1)))
    arr2 = (list(map(lambda x:format(x,'b'),arr2)))

    row=''
    for i in range(n):
        arr = str(int(arr1[i])+int(arr2[i])).zfill(n)
        for j in arr:
            if j == '0':
                row+=' '
            else:
                row+='#'
        answer.append(row)
        row=''

    return answer
