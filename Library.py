class Book:
    def __init__(self, title, author, year, price, stoplist=False):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist

    def get_info(self):
        """Prints author, title, year, price, stoplist."""
        print(f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Price: {self.price}, Stoplist: {self.stoplist}")

    def set_stoplist(self, stoplist):
        """Sets the stoplist status for the book."""
        self.stoplist = stoplist

    @staticmethod
    def find_most_expensive_book(book_list):
        """Finds the most expensive book in a list of books."""
        if not book_list:
            return None
        return max(book_list, key=lambda book: book.price)

    def censor(self, author_name, stoplist_status):
        """
        If the book's author matches the given author_name, 
        set the stoplist status to the provided boolean value.
        """
        if self.author == author_name:
            self.stoplist = stoplist_status
