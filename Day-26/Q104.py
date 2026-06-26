score = 0

print("Quiz Application")

print("1. What is the capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Kolkata")

answer = input("Enter your answer: ")

if answer.lower() == "b":
    score += 1


print("2. Python is a?")
print("a) Programming language")
print("b) Game")
print("c) Browser")

answer = input("Enter your answer: ")

if answer.lower() == "a":
    score += 1


print("Your score:", score, "/2")
