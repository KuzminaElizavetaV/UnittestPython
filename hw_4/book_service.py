from copy import deepcopy


class Book:
    def __init__(self, book_id: str, title: str = None, author: str = None):
        self.book_id = book_id
        self.title = title
        self.author = author

    # Сравнение объектов по атрибутам
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (
            self.book_id == other.book_id
            and self.title == other.title
            and self.author == other.author
        )

    def get_id(self):
        return self.book_id

    def set_id(self, book_id: str):
        self.book_id = book_id

    def get_title(self):
        return self.title

    def set_title(self, title: str):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author: str):
        self.author = author


class BookRepository:
    def __init__(self):
        self._books = []

    def find_by_id(self, book_id: str) -> Book | None:
        for book in self._books:
            if book.id == book_id:
                return book

    def find_all(self) -> list[Book]:
        return deepcopy(self._books)


class BookService:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    @property
    def book_repository(self):
        return self._book_repository

    def find_book_by_id(self, book_id: str) -> Book:
        return self._book_repository.find_by_id(book_id)

    def find_all_books(self) -> list[Book]:
        return self._book_repository.find_all()
