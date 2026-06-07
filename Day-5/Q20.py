# Find Largest Prime Factor

num = int(input("Enter a number: "))
largest_prime = 1

factor = 2

while factor <= num:
    if num % factor == 0:
        largest_prime = factor
        num //= factor
    else:
        factor += 1

print("Largest Prime Factor:", largest_prime)
