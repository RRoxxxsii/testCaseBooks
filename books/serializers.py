from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        isbn = attrs.get('isbn')
        if len(isbn) != 13:
            raise serializers.ValidationError('ISBN не валиден')
        return attrs
