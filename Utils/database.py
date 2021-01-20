import csv
"""
books stored in this file
"""
books_extra = []

books = [
    {
        'name': 'Dune',
        'author': 'Frank Herbert',
        'read': False
    },
    {
        'name': 'Pan Tadeusz',
        'author': 'Adam Mickiewicz',
        'read': False
    },
    {
        'name': 'Hobbit',
        'author': 'J.R.R. Tolkien',
        'read': True
    }
]


def prompt_add_book():
    name = input("Enter the Book title: ").capitalize()
    author = input("Enter the Books author: ").capitalize()
    read = (input("have you read the Book? y/n: ").lower())
    while read not in ['y', 'n']:
        read = (input("have you read the Book? (y)es or (n)ot: ").lower())
    else:
        if read == 'y':
            read = True
        elif read == 'n':
            read = False

    books.append({
        'name': name,
        'author': author,
        'read': read
    })
    print("Thank you! Your book is added")


def list_books():
    for book in books:
        if book['read'] is True:
            read = 'read'
        else:
            read = 'not read'
        print(f'{book["name"]} by {book["author"]}, {read}')


def prompt_read_book():
    name = input('\nWhat book are you looking for? ').lower()
    counter = []
    for book in books:
        if book['name'].lower() == name:
            user_input = input(f"\n{name.capitalize()} by {book['author']} "
                               f"- Would you like to mark it as read? If yes type 'y' ").lower()
            if user_input == 'y':
                book['read'] = True
            counter.append(book)
    if len(counter) == 0:
        print(f"{name} is not in your library")


def prompt_delete_book():
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


def read_extra_books():
    with open('Utils/books.csv', 'r') as books_base:
        reader = csv.DictReader(books_base)
        counter = 0
        for line in reader:
            name = line['name']
            author = line['author']
            read = line['read']
            books.append({'name': name, 'author': author, 'read': read})
            books_extra.append({'name': name, 'author': author, 'read': read})
            counter += 1
        print(f'{counter} added book(s)')


def save_books():
    with open('Utils/books.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'author', 'read'])
        writer.writeheader()
        writer.writerows(books)
