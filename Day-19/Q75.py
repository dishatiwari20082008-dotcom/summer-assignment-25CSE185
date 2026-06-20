r = int(input("Rows: "))
c = int(input("Columns: "))

matrix = []

for i in range(r):
    matrix.append(list(map(int,input().split())))

transpose = []

for j in range(c):
    row = []
    for i in range(r):
        row.append(matrix[i][j])
    transpose.append(row)

print(transpose)
