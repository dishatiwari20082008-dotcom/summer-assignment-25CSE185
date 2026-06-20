r = int(input("Rows: "))
c = int(input("Columns: "))

a = []
b = []

print("Enter first matrix:")
for i in range(r):
    a.append(list(map(int, input().split())))

print("Enter second matrix:")
for i in range(r):
    b.append(list(map(int, input().split())))

result = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(a[i][j] + b[i][j])
    result.append(row)

print(result)
