from django.db.models import QuerySet

from books.models import Book


class BookCrud:

    @staticmethod
    def get_all_books() -> QuerySet[Book]:
        return Book.objects.all()
