from rest_framework.viewsets import ModelViewSet

from books.crud import BookCrud
from books.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = BookCrud.get_all_books()
