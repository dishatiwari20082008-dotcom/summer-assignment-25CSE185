# Reverse Star Pyramid

rows = 5

for i in range(rows):
    spaces = " " * i
    stars = "*" * (2 * (rows - i) - 1)
    print(spaces + stars)
