from django.db.models import QuerySet

from accounts.models import NewUser


class UserCrud:

    @staticmethod
    def get_all_users() -> QuerySet[NewUser]:
        return NewUser.objects.all()
