from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Суперпользователь должен быть is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError('Необходимо предоставить адрес электронной почты')

        if not user_name:
            raise ValueError('Необходимо предоставить ник')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        'Почтовый адрес',
        unique=True,
        error_messages={'unique': 'Указанный почтовый адрес уже занято.'},
        db_index=True
    )
    user_name = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        db_index=True,
        error_messages={'unique': 'Указанное имя уже занято.'}
    )
    created = models.DateTimeField('Дата регистрации', default=timezone.now)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_name'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ('email', )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.user_name
