import json

# Library ko store karne ke liye ek list banaye
library = []

# Menu dikhane ka function
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Book add karne ka function
def add_book():
    print("\nAdd a Book")
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"
    
    # Book ko dictionary mein store karo
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    
    # Book ko library mein add karo
    library.append(book)
    print("Book added successfully!")

# Book remove karne ka function
def remove_book():
    print("\nRemove a Book")
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"] == title:
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found!")

# Book search karne ka function
def search_book():
    print("\nSearch for a Book")
    print("Search by:")
    print("1. Title")
    print("2. Author")
    search_choice = input("Enter your choice: ")
    
    if search_choice == "1":
        title = input("Enter the title: ")
        matching_books = [book for book in library if book["title"] == title]
    elif search_choice == "2":
        author = input("Enter the author: ")
        matching_books = [book for book in library if book["author"] == author]
    else:
        print("Invalid choice!")
        return
    
    if matching_books:
        print("\nMatching Books:")
        for i, book in enumerate(matching_books, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.")

# Saari books display karne ka function
def display_all_books():
    if not library:
        print("\nYour library is empty.")
        return
    
    print("\nYour Library:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

# Statistics display karne ka function
def display_statistics():
    total_books = len(library)
    read_books = sum(book["read"] for book in library)
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    
    print("\nLibrary Statistics:")
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read}%")

# Library ko file mein save karne ka function
def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file)
    print("\nLibrary saved to file.")

# Library ko file se load karne ka function
def load_library():
    global library
    try:
        with open("library.txt", "r") as file:
            library = json.load(file)
        print("\nLibrary loaded from file.")
    except FileNotFoundError:
        print("\nNo saved library found.")

# Main program
def main():
    load_library()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_all_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("\nLibrary saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Program ko run karo
if __name__ == "__main__":
    main()