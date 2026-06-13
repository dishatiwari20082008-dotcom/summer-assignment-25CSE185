def armstrong(num):
    original = num
    sum = 0
    digits = len(str(num))

    while num > 0:
        digit = num % 10
        sum = sum + digit ** digits
        num = num // 10

    if original == sum:
        return True
    else:
        return False


n = int(input("Enter number: "))

if armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
