n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False

if flag:
    print("Symmetric Matrix")
else:
    print("Not Symmetric Matrix")
