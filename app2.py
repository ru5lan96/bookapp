books = {}

def add_book():
    name = input("Type name: ")
    author = input("Type author: ")
    books[name] = author
    print(f"The '{name}' book is added.")

def print_books():
    if books:
        for name, author in books.items():
            print(f"Name: {name}, Author: {author}")
    else:
        print("Book list is empty.")

while True:
    print("\n1. Add Book")
    print("2. Print All Books")
    print("3. Quit")

    number = input("Type: ")

    if number == '1':
        add_book()
    elif number == '2':
        print_books()
    elif number == '3':
        break
    else:
        print("Type error. Please try again.")
