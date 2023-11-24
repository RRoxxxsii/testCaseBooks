from rest_framework.generics import CreateAPIView

from accounts.crud import UserCrud
from accounts.serializers import UserSerializer
from accounts.tasks import send_registration_email


class RegisterUser(CreateAPIView):
    """
    Регистрация - Создание пользователя.
    """
    queryset = UserCrud.get_all_users()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        resp = super().create(request, *args, **kwargs)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=False)
        email = serializer.data.get('email')
        user_name = serializer.data.get('email')
        send_registration_email.delay(
            recipient_email=email,
            template_name='email/greeting_email.txt',
            data={'user_name': user_name},
            subject='Регистрация на сайте..'
        )
        return resp
