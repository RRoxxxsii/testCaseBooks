from rest_framework import serializers

from accounts.models import NewUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        fields = ('user_name', 'email')
