str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common = ""

for char in str1:
    if char in str2 and char not in common:
        common += char

print("Common characters:", common)
