books= ["Shatter me", "Five Survive", "Six of Crows", "One of us is lying"]
def show_books():
    print("\nBOOKS IN LIBRARY📚")
    for book in books:
        print("-" + book )
def borrow_book(): 
    name=input("Enter the book name you want to borrow:")
    if name in books:
        books.remove(name)
        print(f"YOU BORROWED:", {name})
    else: 
        print("book not available❌")
def return_books():
    name=input("enter the book name you want to return:")
    books.append(name)
    print(f"YOU RETURNED BOOK", {name})
while True:
    print("\n what do you want to do?")
    print("view book list")
    print("borrow a book")
    print("return a book")
    print("exit")

    choice = input("choose(1-4):")
    if choice == '1':
        show_books()
    elif choice == '2': 
        borrow_book()
    elif choice == '3': 
        return_books()
    elif choice == '4':
        break
    else: 
        print("invalid choice")






  