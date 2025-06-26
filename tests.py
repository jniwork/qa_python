from conftest import *
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book(horror_genre_book)

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_add_book_more_then_40_symbols(self, collector):
        name = 'string more then 40 symbols string more then 40 symbols'
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_book_with_0_symbols(self, collector):
        name = ''
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_two_similar_books(self, collector):
        collector.add_new_book(comedy_genre_book)
        collector.add_new_book(comedy_genre_book)

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_without_genre(self, collector):
        collector.add_new_book(horror_genre_book)

        assert collector.get_books_genre().get(horror_genre_book) == ''

    def test_set_book_genre_set_genre(self, books_collector):
        assert books_collector.get_book_genre(horror_genre_book) == 'Ужасы'

    def test_get_books_with_specific_genre_one_book_get_list_genre(self, books_collector):
        genre = 'Детективы'

        assert books_collector.get_books_with_specific_genre(genre) == [detective_genre_book]

    def test_get_books_for_children_get_list_book(self, books_collector):
        assert books_collector.get_books_for_children() == [fantasy_genre_book, child_genre_book, comedy_genre_book]

    @pytest.mark.parametrize(
        'book, expected_result',
        [
            (fantasy_genre_book, True),
            (horror_genre_book, False),
            (detective_genre_book, True),
            (child_genre_book, True),
            (comedy_genre_book, True),
        ]
    )
    def test_get_books_for_children_adult_books_not_included_the_list(self, collector, books_collector, book, expected_result):
        children_books = collector.get_books_for_children()
        assert (book in children_books) == expected_result

    def test_add_book_in_favorites_add_one_book(self, collector, books_collector):
        collector.add_book_in_favorites(fantasy_genre_book)
        assert collector.get_list_of_favorites_books() == [fantasy_genre_book]

    def test_add_book_in_favorites_similar_books(self, collector, books_collector):
        collector.add_book_in_favorites(horror_genre_book)
        collector.add_book_in_favorites(horror_genre_book)

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_to_favorites_unlisted_books(self, collector):
        collector.add_book_in_favorites('Книга не из списка')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_removes_book(self, collector, books_collector):
        collector.add_book_in_favorites(fantasy_genre_book)
        collector.delete_book_from_favorites(fantasy_genre_book)

        assert len(collector.get_list_of_favorites_books()) == 0
