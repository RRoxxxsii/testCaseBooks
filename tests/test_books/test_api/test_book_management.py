import json

import pytest
from django.urls import reverse
from rest_framework import status


class TestBookViewSet:
    url = 'book-list'
    url_detail = 'book-detail'

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        'title, author, year_published, isbn, validity_status',
        [
            ('Война и Мир', 'Л.Н. Толстой', 1867, '1010101010101', status.HTTP_201_CREATED),
            ('Война и Мир', 'Л.Н. Толстой', 1867, '1010', status.HTTP_400_BAD_REQUEST)       # isbn not valid
        ]
    )
    def test_create_book(
            self, api_client, title, author, year_published, isbn, validity_status
    ):
        response = api_client.post(reverse(self.url), data={
            'title': title, 'author': author, 'year_published': year_published, 'isbn': isbn
        })
        assert response.status_code == validity_status

    @pytest.mark.django_db
    def test_get_all_books(self, api_client, book_1, book_2):
        response = api_client.get(reverse(self.url))

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content.decode())) == 2

    @pytest.mark.django_db
    def test_get_one_book(self, api_client, book_1, book_2):
        response = api_client.get(reverse(self.url_detail, args=[book_1.pk]))
        assert response.status_code == status.HTTP_200_OK
        assert json.loads(response.content.decode()).get('id') == book_1.pk

    @pytest.mark.django_db
    def test_delete_book(self, api_client, book_1, book_2):
        response = api_client.delete(reverse(self.url_detail, args=[book_1.pk]))
        assert response.status_code == status.HTTP_204_NO_CONTENT

    @pytest.mark.django_db
    def test_update_book(self, api_client, book_1, book_2):
        isbn_before_update = book_1.isbn
        response = api_client.patch(reverse(self.url_detail, args=[book_1.pk]), data={
            'isbn': '1011110111101'
        })
        book_1.refresh_from_db()
        assert response.status_code == status.HTTP_200_OK
        assert isbn_before_update != book_1.isbn
