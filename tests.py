import pytest
from main import BooksCollector

fantasy_genre_book = 'Армагеддон на минималках'
horror_genre_book = 'Оно смотрит из подвала'
detective_genre_book = 'Инспектор Пельмень'
child_genre_book = 'Приключения Пятачка и огурца'
comedy_genre_book = 'Как выжить на семейном ужине'


class TestBooksCollector:

    def test_add_new_book_adds_book(self, collector):
        collector.add_new_book(horror_genre_book)

        assert horror_genre_book in collector.books_genre
        assert len(collector.books_genre) == 1

    def test_add_new_book_does_not_add_book_with_name_over_40_chars(self, collector):
        name = 'string more then 40 symbols string more then 40 symbols'
        collector.add_new_book(name)

        assert name not in collector.books_genre
        assert len(collector.books_genre) == 0

    def test_add_new_book_does_not_add_book_with_empty_name(self, collector):
        name = ''
        collector.add_new_book(name)

        assert name not in collector.books_genre
        assert len(collector.books_genre) == 0

    def test_add_new_book_does_not_add_duplicate_books(self, collector):
        collector.add_new_book(comedy_genre_book)
        collector.add_new_book(comedy_genre_book)

        assert len(collector.books_genre) == 1

    def test_set_book_genre_sets_genre(self, collector):
        collector.add_new_book(horror_genre_book)
        collector.set_book_genre(horror_genre_book, 'Ужасы')

        assert collector.books_genre[horror_genre_book] == 'Ужасы'

    def test_get_book_genre_returns_genre(self, collector):
        collector.books_genre[detective_genre_book] = 'Детективы'

        assert collector.get_book_genre(detective_genre_book) == 'Детективы'

    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        collector.books_genre[detective_genre_book] = 'Детективы'
        collector.books_genre[fantasy_genre_book] = 'Фантастика'

        result = collector.get_books_with_specific_genre('Детективы')
        assert result == [detective_genre_book]

    def test_get_books_genre_returns_correct_dictionary(self, collector):
        collector.add_new_book(fantasy_genre_book)
        collector.set_book_genre(fantasy_genre_book, 'Фантастика')

        collector.add_new_book(child_genre_book)
        collector.set_book_genre(child_genre_book, 'Мультфильмы')

        expected_result = {
            fantasy_genre_book: 'Фантастика',
            child_genre_book: 'Мультфильмы',
        }

        assert collector.get_books_genre() == expected_result

    def test_get_books_for_children_excludes_adult_books(self, collector):
        collector.books_genre[fantasy_genre_book] = 'Фантастика'
        collector.books_genre[child_genre_book] = 'Мультфильмы'
        collector.books_genre[comedy_genre_book] = 'Комедии'
        collector.books_genre[horror_genre_book] = 'Ужасы'

        result = collector.get_books_for_children()
        assert horror_genre_book not in result
        assert sorted(result) == sorted([fantasy_genre_book, child_genre_book, comedy_genre_book])

    @pytest.mark.parametrize(
        'book, genre, expected_result',
        [
            (fantasy_genre_book, 'Фантастика', True),
            (horror_genre_book, 'Ужасы', False),
            (detective_genre_book, 'Детективы', False),
            (child_genre_book, 'Мультфильмы', True),
            (comedy_genre_book, 'Комедии', True),
        ]
    )
    def test_get_books_for_children_parametrized(self, collector, book, genre, expected_result):
        collector.books_genre[book] = genre

        result = collector.get_books_for_children()
        assert (book in result) == expected_result

    def test_add_book_in_favorites_adds_book(self, collector):
        collector.books_genre[fantasy_genre_book] = 'Фантастика'
        collector.add_book_in_favorites(fantasy_genre_book)

        assert collector.favorites == [fantasy_genre_book]

    def test_add_book_in_favorites_does_not_add_duplicate(self, collector):
        collector.books_genre[horror_genre_book] = 'Ужасы'
        collector.add_book_in_favorites(horror_genre_book)
        collector.add_book_in_favorites(horror_genre_book)

        assert collector.favorites == [horror_genre_book]

    def test_add_book_in_favorites_ignores_unknown_book(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')

        assert collector.favorites == []

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.books_genre[fantasy_genre_book] = 'Фантастика'
        collector.add_book_in_favorites(fantasy_genre_book)

        collector.delete_book_from_favorites(fantasy_genre_book)

        assert collector.favorites == []

    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.add_new_book(fantasy_genre_book)
        collector.set_book_genre(fantasy_genre_book, 'Фантастика')
        collector.add_new_book(child_genre_book)
        collector.set_book_genre(child_genre_book, 'Мультфильмы')

        collector.add_book_in_favorites(fantasy_genre_book)
        collector.add_book_in_favorites(child_genre_book)

        expected_result = [fantasy_genre_book, child_genre_book]

        assert collector.get_list_of_favorites_books() == expected_result
