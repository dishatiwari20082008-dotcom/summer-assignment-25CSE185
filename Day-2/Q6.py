num = int(input("Enter a number: "))
temp = abs(num)
rev = 0

while temp > 0:
    rev = rev * 10 + (temp % 10)
    temp //= 10

if num < 0:
    rev = -rev

print("Reversed number =", rev)
