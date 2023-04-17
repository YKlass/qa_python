import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def book_name():
    return 'Гордость и предубеждение и зомби'