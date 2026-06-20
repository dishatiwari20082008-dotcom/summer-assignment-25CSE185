r = int(input())
c = int(input())

matrix = []

for i in range(r):
    matrix.append(list(map(int,input().split())))

for row in matrix:
    print(sum(row))
