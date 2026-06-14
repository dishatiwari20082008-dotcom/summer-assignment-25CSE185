def find_duplicates(arr):
    duplicates = []

    for i in arr:
        if arr.count(i) > 1 and i not in duplicates:
            duplicates.append(i)

    return duplicates


arr = []

n = int(input("Enter size of array: "))

for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Duplicate elements are:", find_duplicates(arr))
