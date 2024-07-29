import LibraryManager as lm

books_data = [
    ("978-0134685991", "Operating Systems: Three Easy Pieces", "Remzi H. Arpaci-Dusseau", "Arpaci-Dusseau Books", 1, 2020, "Operating Systems"),
    ("978-0134093413", "Operating System Concepts", "Abraham Silberschatz", "Wiley", 10, 2022, "Operating Systems"),
    ("978-0134190440", "Modern Operating Systems", "Andrew S. Tanenbaum", "Pearson", 4, 2022, "Operating Systems"),
    ("978-0262033848", "Introduction to Algorithms", "Thomas H. Cormen", "MIT Press", 4, 2020, "Data Structures"),
    ("978-0134687476", "Data Structures and Algorithm Analysis in C++", "Mark Allen Weiss", "Pearson", 4, 2021, "Data Structures"),
    ("978-0321573513", "Algorithms", "Robert Sedgewick", "Addison-Wesley", 4, 2020, "Data Structures"),
    ("978-1789950734", "Python Machine Learning", "Sebastian Raschka", "Packt", 3, 2020, "Machine Learning"),
    ("978-1492051138", "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Aurélien Géron", "O'Reilly Media", 2, 2020, "Machine Learning"),
    ("978-1617294433", "Grokking Deep Learning", "Andrew W. Trask", "Manning Publications", 1, 2019, "Machine Learning"),
    ("978-1108470420", "Machine Learning: A Probabilistic Perspective", "Kevin P. Murphy", "MIT Press", 1, 2020, "Machine Learning"),
]

for isbn, title, author, publisher, volume, year, topic in books_data:
    lm.add_book(isbn, title, author, publisher, volume, year, topic)

lm.remove_book("978-0134687476")

lm.retrieve_book("978-0134685991")

lm.search_books_by_title_or_author("Operating System")

lm.list_all_books()

lm.update_book_details("978-0134093413", title="Operating System Concepts Updated")

lm.check_book_availability("978-0134093413")
