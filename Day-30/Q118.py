books = []

n = int(input("Enter number of books: "))

for i in range(n):
    book = input("Enter book name: ")
    books.append(book)

print("\nAvailable Books:")

for b in books:
    print(b)

search = input("Enter book to search: ")

if search in books:
    print("Book available")
else:
    print("Book not available")
