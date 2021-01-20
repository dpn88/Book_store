from Utils import database


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in menu_choice:
            selected_function = menu_choice[user_input]
            selected_function()
        user_input = input(USER_CHOICE)


USER_CHOICE = """
Enter:
- 'a' ta add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
- 'e' to read more books from database
- 's' to save your library to database - not implemented yet
"""

menu_choice = {
    'a': database.prompt_add_book,
    'l': database.list_books,
    'r': database.prompt_read_book,
    'd': database.prompt_delete_book,
    'e': database.read_extra_books,
    's': database.save_books
}


menu()
