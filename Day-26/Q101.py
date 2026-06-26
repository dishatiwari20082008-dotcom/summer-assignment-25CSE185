import random

number = random.randint(1, 100)

guess = int(input("Guess the number (1-100): "))

if guess == number:
    print("Correct guess!")
elif guess < number:
    print("Too low!")
else:
    print("Too high!")

print("The number was:", number)
