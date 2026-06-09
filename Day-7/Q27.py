# Recursive Sum of Digits

def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

num = int(input("Enter a number: "))
print("Sum of Digits =", sum_digits(num))
