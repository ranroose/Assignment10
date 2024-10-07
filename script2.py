#
from Library import Book

#a list of different books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 10.99)
book2 = Book("1984", "George Orwell", 1949, 8.99)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960, 12.99)
book4 = Book("Moby-Dick", "Herman Melville", 1851, 7.50, stoplist=True)
book5 = Book("War and Peace", "Leo Tolstoy", 1869, 20.00)

#a list of books
book_list = [book1, book2, book3, book4, book5]

#info for each book
print("Information for each book:")
for book in book_list:
    book.get_info()

#the most expensive book
most_expensive_book = Book.find_most_expensive_book(book_list)
if most_expensive_book:
    print("\nThe most expensive book is:")
    most_expensive_book.get_info()

#censor a book by author
print("\nApplying censor on George Orwell's books...")
for book in book_list:
    book.censor("George Orwell", True)

# updated book info after censoring
print("\nUpdated book information after censoring:")
for book in book_list:
    book.get_info()

#stoplist manually for a book
print("\nSetting stoplist for 'War and Peace' to True.")
book5.set_stoplist(True)

#final book info
print("\nFinal book information after manual stoplist:")
for book in book_list:
    book.get_info()
