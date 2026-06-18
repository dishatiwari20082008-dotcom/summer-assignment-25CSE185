# Sort array in descending order

arr = [5, 2, 9, 1, 7]

n = len(arr)

for i in range(n):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Descending order:", arr)
