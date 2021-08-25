r, c =map(int,input().split())
matrix1 = [list(map(int, list(input()))) for _ in range(r)]
matrix2 = [list(map(int, list(input()))) for _ in range(r)]
answer=0

def checkEquality():
    for i in range(r):
        for j in range(c):
            if matrix1[i][j] !=matrix2[i][j]:
                return 0
    return 1

for i in range(0,r-2):
    for j in range (0,c-2):
        if matrix1[i][j]!=matrix2[i][j]:
            for k in range(i,i+3):
                for l in range(j,j+3):
                    matrix1[k][l] = 1 - matrix1[k][l]
            answer +=1


if checkEquality():
    print(answer)
else:
    print(-1)
    
    
 #https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=pjok1122&logNo=221652193756
