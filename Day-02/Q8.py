num = int(input("Enter a number: "))
temp = abs(num)
original = temp
rev = 0

while temp > 0:
    rev = rev * 10 + (temp % 10)
    temp //= 10

if original == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
