def display_array(arr):
    print("Array elements are:")

    for i in arr:
        print(i)


arr = []

n = int(input("Enter size of array: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

display_array(arr)
