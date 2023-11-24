import pytest

from books.models import Book


@pytest.fixture()
def book_1(db) -> Book:
    return Book.objects.create(
        title='Преступление и наказание',
        author='Ф.М. Достоевский',
        year_published=1866,
        isbn='1010101010101'
    )


@pytest.fixture()
def book_2(db) -> Book:
    return Book.objects.create(
        title='Книга...',
        author='Автор...',
        year_published=1800,
        isbn='1010101010100'
    )
