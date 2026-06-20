r1 = int(input())
c1 = int(input())

a = []

for i in range(r1):
    a.append(list(map(int,input().split())))

r2 = int(input())
c2 = int(input())

b = []

for i in range(r2):
    b.append(list(map(int,input().split())))

result = [[0]*c2 for i in range(r1)]

for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result[i][j] += a[i][k] * b[k][j]

print(result)
