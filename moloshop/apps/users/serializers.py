
# moloshop/apps/users/serializers.py

from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователя.
    - Принимает email, пароль и дополнительные поля (например, никнейм)
    - Создаёт пользователя с помощью create_user (используйте ваш UserManager)
    """
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    nickname = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'nickname')  # можно добавить еще поля по необходимости

    def create(self, validated_data):
        # User.objects.create_user управляет хешированием пароля
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            nickname=validated_data.get('nickname', '')
        )
        return user
