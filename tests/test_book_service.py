import unittest
from unittest.mock import Mock
from copy import deepcopy
from hw_4.book_service import BookService, Book


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_repository = Mock()
        self.book_service = BookService(book_repository=self.mock_repository)

    def test_find_book_by_id(self):
        expected_book = Book(book_id="2456", title="Новый сладостный стиль", author="Василий Аксенов")
        self.mock_repository.find_by_id.return_value = expected_book

        result = self.book_service.find_book_by_id(book_id="2456")

        self.mock_repository.find_by_id.assert_called_once_with("2456")
        self.assertEqual(result, expected_book)

    def test_find_all_books(self):
        expected_books = [
            Book(book_id="1", title="Курс активного трейдера", author="Александр Герчик"),
            Book(book_id="2", title="За гранью японских свечей", author="Стив Нисон"),
            Book(book_id="3", title="Дворянское гнездо. Накануне", author="Иван Тургенев"),
            Book(book_id="4", title="И даже небо было нашим", author="Паоло Джордано"),
            Book(book_id="5", title="Год нашей любви", author="Сарина Боуэн"),
            Book(book_id="6", title="Ведьмина роща", author="Елена Абрамкина"),
        ]
        self.mock_repository.find_all.return_value = deepcopy(expected_books)

        result = self.book_service.find_all_books()

        self.mock_repository.find_all.assert_called_once()
        self.assertEqual(result, expected_books)


if __name__ == "__main__":
    unittest.main()
