books = {}

book_id = input("Enter book ID: ")
book_name = input("Enter book name: ")
author = input("Enter author name: ")

books[book_id] = {
    "Book Name": book_name,
    "Author": author
}

print("\nLibrary Record")
print("Book ID:", book_id)
print("Book Name:", books[book_id]["Book Name"])
print("Author:", books[book_id]["Author"])
