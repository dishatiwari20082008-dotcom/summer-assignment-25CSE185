def palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return True
    else:
        return False


n = int(input("Enter number: "))

if palindrome(n):
    print("Palindrome number")
else:
    print("Not a palindrome number")
