def sum_average(arr):
    total = sum(arr)
    average = total / len(arr)

    print("Sum =", total)
    print("Average =", average)


arr = []

n = int(input("Enter size of array: "))

for i in range(n):
    arr.append(int(input("Enter element: ")))

sum_average(arr)
