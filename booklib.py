books = []
issued_books = []

# ADD BOOKS
def add_books():
    name = input("enter the book name: ")
    books.append(name)
    print("book added")

# SHOW BOOKS
def show_books():
    if len(books) == 0:
        print("no books available")
    else:
        print("books available")
        for b in books:
            print(b)

# ISSUE BOOK
def issue_books():
    name = input("enter the book name: ")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print("book issued")
    else:
        print("book not available")

# RETURN BOOK
def return_books():
    name = input("enter the book name: ")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print("book returned")
    else:
        print("book not issued")

# MAIN BODY
def library():
    while True:
        print("\n1. add books")
        print("2. show books")
        print("3. issue books")
        print("4. return books")
        print("5. exit")

        choice = int(input("enter your choice: "))

        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("thank you")
            break
        else:
            print("invalid choice")

library()
