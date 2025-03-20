books = []

while True:
    print("\n1. Add Book")
    print("2. Print All Books")
    print("3. Quit")

    number = input("Type: ")

    if number == '1':
        name = input("Type name: ")
        author = input("Type author: ")
        books.append((name, author))
        print(f"The '{name}' book is added.")
    elif number == '2':
        if books:
            for i in range(len(books)):
                print(f"{i + 1}. Name: {books[i][0]}, Author: {books[i][1]}")

        else:
            print("Book list is empty.")
    elif number == '3':
        break
    else:
        print("Type error. Please try again.")
