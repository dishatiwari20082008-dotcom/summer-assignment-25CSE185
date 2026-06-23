string = input("Enter a string: ")

for char in string:
    if string.count(char) > 1:
        print("First repeating character:", char)
        break
else:
    print("No repeating character found")
