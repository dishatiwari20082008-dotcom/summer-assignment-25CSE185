# Find maximum frequency element

arr = [1, 2, 3, 2, 2, 4, 1]

frequency = {}

for i in arr:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

max_element = max(frequency, key=frequency.get)

print("Maximum frequency element:", max_element)
