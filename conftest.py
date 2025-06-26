import pytest
from main import BooksCollector


@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector


fantasy_genre_book = 'Армагеддон на минималках'
horror_genre_book = 'Оно смотрит из подвала'
detective_genre_book = 'Инспектор Пельмень'
child_genre_book = 'Приключения Пятачка и огурца'
comedy_genre_book = 'Как выжить на семейном ужине'


@pytest.fixture(scope='function')
def books_collector(collector):
    books_genre = [
        (fantasy_genre_book, 'Фантастика'),
        (horror_genre_book, 'Ужасы'),
        (detective_genre_book, 'Детективы'),
        (child_genre_book, 'Мультфильмы'),
        (comedy_genre_book, 'Комедии'),
    ]

    for book, genre in books_genre:
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

    return collector
