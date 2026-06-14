def frequency(arr, element):
    count = 0

    for i in arr:
        if i == element:
            count += 1

    return count


arr = []

n = int(input("Enter size of array: "))

for i in range(n):
    arr.append(int(input("Enter element: ")))

element = int(input("Enter element to find frequency: "))

print("Frequency =", frequency(arr, element))
