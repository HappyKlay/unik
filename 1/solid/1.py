class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_book_details(self):
        return f"{self.title} by {self.author}"


class BookRepository:
    def save_to_database(self, book):
        # Уявімо, що тут логіка збереження у базу даних
        print(f"Saving '{book.title}' to the database.")
