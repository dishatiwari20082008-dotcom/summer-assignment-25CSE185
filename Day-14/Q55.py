def second_largest(arr):
    arr.sort()

    return arr[-2]


arr = []

n = int(input("Enter size of array: "))

for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Second largest element =", second_largest(arr))
