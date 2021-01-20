import csv
"""
functions needed by main file to process data stored in books.csv
"""

books = []
# list populated by other functions and used to save data
# fetched from the books.csv in the memory and to operate on the data


def prompt_add_book():  # adds a book to the books.csv file and prompts was the book read or not
    read_books()
    name = input("Enter the Book title: ").capitalize()
    author = input("Enter the Books author: ").capitalize()
    read = (input("have you read the Book? y/n: ").lower())
    while read not in ['y', 'n']:
        read = (input("have you read the Book? (y)es or (n)ot: ").lower())
    else:
        if read == 'y':
            read = 'True'
        elif read == 'n':
            read = 'False'

    books.append({
        'name': name,
        'author': author,
        'read': read
    })
    print("Thank you! Your book is added")
    save_books()
    books.clear()


def list_books():   # fetches the data from books.csv na prints it out
    read_books()
    library = books
    for book in library:
        if book['read'] == 'True':
            read = 'read'
        else:
            read = 'not read'
        print(f'{book["name"]} by {book["author"]}, {read}')
    books.clear()


def prompt_read_book():     # allows to mark a book as "read" and checks was the book already marked or not
    read_books()
    name = input('\nWhat book are you looking for? ').lower()
    counter = []
    for book in books:
        if book['name'].lower() == name:
            if book['read'] == 'True':
                print(f'Book {book["name"]} was marked as read already')
            else:
                user_input = input(f"\n{name.capitalize()} by {book['author']} "
                                   f"- Would you like to mark it as read? If yes type 'y' ").lower()
                if user_input == 'y':
                    book['read'] = 'True'
            counter.append(book)
    if len(counter) == 0:
        print(f"{name} is not in your library")
    save_books()
    books.clear()


def prompt_delete_book():   # deletes a book from the database
    read_books()
    name = input('\nWhat book would you like to delete? ').lower()
    for i in range(len(books)):
        if books[i]['name'].lower() == name:
            user_input = input(f"\n{books[i]['name'].capitalize()} by {books[i]['author']} "
                               f"- Would you like to remove it? To confirm type: 'y' ").lower()
            if user_input == 'y':
                print(f'{books[i]["name"]} was deleted from your library')
                del books[i]
                break
    else:
        print(f"{name.capitalize()} is not in your library")
    save_books()
    books.clear()


def read_books():   # function used by other functions to fetch data from database
    with open('Utils/books.csv', 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            name = line['name']
            author = line['author']
            read = line['read']
            books.append({'name': name, 'author': author, 'read': read})


def save_books():   # function used by other functions to save data to database
    with open('Utils/books.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'author', 'read'])
        writer.writeheader()
        writer.writerows(books)
