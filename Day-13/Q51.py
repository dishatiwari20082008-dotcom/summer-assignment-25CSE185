def largest_smallest(arr):
    print("Largest =", max(arr))
    print("Smallest =", min(arr))


arr = []

n = int(input("Enter size of array: "))

for i in range(n):
    arr.append(int(input("Enter element: ")))

largest_smallest(arr)
