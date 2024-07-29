library = {}

def add_book(isbn, title, author, publisher, volume, year, topic):
    if isbn not in library:
        library[isbn] = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'volume': volume,
            'year': year,
            'topic': topic
        }
        print(f"Book '{title}' added successfully.")
    else:
        print(f"Book with ISBN {isbn} already exists.")

def remove_book(isbn):
    if isbn in library:
        removed_book = library.pop(isbn)
        print(f"Book '{removed_book['title']}' removed successfully.")
    else:
        print(f"No book found with ISBN {isbn}.")

def retrieve_book(isbn):
    if isbn in library:
        book = library[isbn]
        print(f"Details of book with ISBN {isbn}: {book}")
    else:
        print(f"No book found with ISBN {isbn}.")

def search_books_by_title_or_author(query):
    results = [book for book in library.values() if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
    if results:
        print(f"Books found for '{query}': {results}")
    else:
        print(f"No books found for '{query}'.")

def list_all_books():
    if library:
        for isbn, book in library.items():
            print(f"ISBN: {isbn}, Details: {book}")
    else:
        print("No books currently in the library.")

def update_book_details(isbn, title=None, author=None, publisher=None, volume=None, year=None, topic=None):
    if isbn in library:
        if title:
            library[isbn]['title'] = title
        if author:
            library[isbn]['author'] = author
        if publisher:
            library[isbn]['publisher'] = publisher
        if volume:
            library[isbn]['volume'] = volume
        if year:
            library[isbn]['year'] = year
        if topic:
            library[isbn]['topic'] = topic
        print(f"Details of book with ISBN {isbn} updated successfully.")
    else:
        print(f"No book found with ISBN {isbn}.")

def check_book_availability(isbn):
    if isbn in library:
        print(f"Book with ISBN {isbn} is available.")
    else:
        print(f"Book with ISBN {isbn} is not available.")
