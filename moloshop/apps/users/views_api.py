
# moloshop/apps/users/views_api.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer
from .models import User

class RegisterAPIView(APIView):
    """
    POST /api/users/register/
    Регистрация пользователя через API.
    """
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'id': str(user.id), 'email': user.email, 'token': str(token)},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    """
    POST /api/users/login/
    Авторизация пользователя: возвращает токен для последующей аутентификации запросов.
    """
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': str(token), 'id': str(user.id)}, status=status.HTTP_200_OK)
        return Response({'error': 'Неверный e-mail или пароль'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    """
    POST /api/users/logout/
    Деактивация (удаление) токена — обычный способ разлогиниться при аутентификации по токену.
    Только для авторизованных пользователей.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Вы успешно вышли'}, status=status.HTTP_200_OK)
