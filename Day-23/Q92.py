string = input("Enter a string: ")

frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

max_char = max(frequency, key=frequency.get)

print("Maximum occurring character:", max_char)
print("Frequency:", frequency[max_char])
