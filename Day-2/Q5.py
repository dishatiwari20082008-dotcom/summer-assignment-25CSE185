num = int(input("Enter a number: "))
temp = abs(num)
sum_digits = 0

while temp > 0:
    sum_digits += temp % 10
    temp //= 10

print("Sum of digits =", sum_digits)
