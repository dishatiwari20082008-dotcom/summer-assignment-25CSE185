r = int(input())
c = int(input())

matrix = []

for i in range(r):
    matrix.append(list(map(int,input().split())))

for j in range(c):
    total = 0
    for i in range(r):
        total += matrix[i][j]
    print(total)
