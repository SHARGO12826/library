import json
import os

FILE_NAME = "library.json"


def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    save_books(books)

    print("Book added successfully!")


def view_books(books):
    if not books:
        print("\nNo books in the library.")
        return

    print("\n===== Library Books =====")

    for book in books:
        print(
            f"ID: {book['id']} | "
            f"Title: {book['title']} | "
            f"Author: {book['author']} | "
            f"Status: {book['status']}"
        )


def search_books(books):
    keyword = input("Enter title or author to search: ").lower()

    results = [
        book for book in books
        if keyword in book["title"].lower()
        or keyword in book["author"].lower()
    ]

    if not results:
        print("No books found.")
        return

    print("\n===== Search Results =====")

    for book in results:
        print(
            f"ID: {book['id']} | "
            f"Title: {book['title']} | "
            f"Author: {book['author']} | "
            f"Status: {book['status']}"
        )


def borrow_book(books):
    try:
        book_id = int(input("Enter book ID to borrow: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                book["status"] = "Borrowed"
                save_books(books)
                print("Book borrowed successfully!")
            else:
                print("This book is already borrowed.")
            return

    print("Book not found.")


def return_book(books):
    try:
        book_id = int(input("Enter book ID to return: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Borrowed":
                book["status"] = "Available"
                save_books(books)
                print("Book returned successfully!")
            else:
                print("This book is already available.")
            return

    print("Book not found.")


def remove_book(books):
    try:
        book_id = int(input("Enter book ID to remove: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_books(books)
            print("Book removed successfully!")
            return

    print("Book not found.")


def main():
    books = load_books()

    while True:
        print("\n==============================")
        print("      LIBRARY ORGANIZER")
        print("==============================")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Remove Book")
        print("7. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)

        elif choice == "2":
            view_books(books)

        elif choice == "3":
            search_books(books)

        elif choice == "4":
            borrow_book(books)

        elif choice == "5":
            return_book(books)

        elif choice == "6":
            remove_book(books)

        elif choice == "7":
            print("Thank you for using Library Organizer!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()