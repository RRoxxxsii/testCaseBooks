from django.db import models


class Book(models.Model):

    title = models.CharField('Название', unique=True, max_length=255)
    author = models.CharField('Автор', max_length=255)
    year_published = models.PositiveIntegerField('Год издания')
    isbn = models.CharField('ISBN', max_length=13, unique=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.author} - {self.title}'
