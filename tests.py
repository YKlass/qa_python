# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_can_add_same_book_only_once(self, collector, book_name):
        collector.add_new_book(book_name)
        total = len(collector.get_books_rating())
        collector.set_book_rating(book_name, 8)
        collector.add_new_book(book_name)
        assert len(collector.get_books_rating()) == total
        assert collector.get_book_rating(book_name) == 8

    def test_set_book_rating_less_than_1_ignored(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, 0)
        assert collector.get_book_rating(book_name) == 1

    def test_set_book_rating_more_than_10_ignored(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, 11)
        assert collector.get_book_rating(book_name) == 1

    def test_get_book_rating_for_unadded_book(self, collector):
        assert collector.books_rating.get('влоа_првоп№р%оврапоушк') is None

    def test_add_book_in_favorites_added_book_is_at_list_of_favorites(self, book_name, collector):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_twice_no_duplicate(self, book_name, collector):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == favorites

    def test_delete_book_from_favorites_deleted_book_is_not_at_list_of_favorites(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_unadded_book_is_not_in_favorites(self, collector, book_name):
        collector.add_book_in_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_get_book_with_specific_rating(self, collector):
        for name, rating in [
            ['Курочка Ряба', 5],
            ['Колобок', 4],
            ['Красная Шапочка', 10],
            ['Теремок', 10]
        ]:
            collector.add_new_book(name)
            collector.set_book_rating(name, rating)
        assert collector.get_books_with_specific_rating(4) == ['Колобок']
