def perfect(num):
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum = sum + i

    if sum == num:
        return True
    else:
        return False


n = int(input("Enter number: "))

if perfect(n):
    print("Perfect number")
else:
    print("Not a perfect number")
