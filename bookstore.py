import sqlite3

# Create an ebookstore database.
db = sqlite3.connect('ebookstore')
cursor = db.cursor()


# Function to enter a new book into ebookstore database.
def add_book():
    id = int(input('Enter the book id here: '))

    # Check if the book exists
    cursor.execute('SELECT * FROM book WHERE id = ?', (id,))
    existing_book = cursor.fetchone()

    if existing_book:
        print(f'Book with ID:{id} already exists.')
    else:
        title = input('Enter the title of the book here: ')
        author = input('Enter the name of the author here: ')
        qty = int(input('Enter the quantity here: '))
    
    # Insert new book.
    cursor.execute('''INSERT INTO book VALUES(?, ?, ?, ?)''',
                       (id, title, author, qty))
    db.commit()
    print(f'{title} with ID:{id} has been added to the database.')


# Function to update a book within the table.
def update_book():
    id = int(input('Enter the book id here: '))
    new_qty = int(input('Enter the new quantity of books here: '))
    cursor.execute('''UPDATE book SET qty = ? WHERE id = ?''',
                    (id, new_qty))
    db.commit()
    print(f'{id} has been updated.')


# Function to delete a specific book from the table
def delete_book():
    id = int(input('Enter book ID: '))
    cursor.execute('''DELETE FROM book WHERE id = ?''', (id,))
    db.commit()
    print(f'{id} has been deleted.')


# Function to enable the user to search for a book in the database.
def search_book():
    search_title = input('Enter the title of the book here: ')
    cursor.execute('''SELECT * FROM book WHERE title = ?''', (search_title,))
    books = cursor.fetchall()
    for book in books:
        print(book)


# Create book table.
cursor.execute(''' CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,
                title TEXT, author TEXT, qty INTEGER)
''')
db.commit()

# List to store book data.
books_data = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, 'Harry Potter and the Philosopher"s Stone', 'J.K Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]

# Populate table with book data.
cursor.executemany('''INSERT INTO book(id, title, author, qty)
                   VALUES(?, ?, ?, ?)''', books_data)
db.commit()

# Menu prompted for user.
while True:
    print('Welcome to the ebook store!')

    print('')

    print('Menu:')
    print('1. Enter a book')
    print('2. Update a book')
    print('3. Delete a book')
    print('4. Search for a book')
    print('0. Exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        add_book()
        print('')
    elif choice == 2:
        update_book()
        print('')
    elif choice == 3:
        delete_book()
        print('')
    elif choice == 4:
        search_book()
        print('')
    elif choice == 0:
        db.close()
        break
    else:
        print('Invalid input please try again.')
        print('')
    
    
