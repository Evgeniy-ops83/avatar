from django.core.mail import send_mail
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Profile
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return Response({'success': 'Вы успешно вошли в систему'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Неверный email или пароль'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_user(request):
    email = request.data.get('email')
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Этот email уже зарегистрирован.'}, status=status.HTTP_400_BAD_REQUEST)

    # Создание пользователя
    user = User.objects.create_user(
        username=email,
        email=email,
        password=request.data.get('password'),
        first_name=request.data.get('name')  # Сохраняем имя
    )
    
    # Отправка письма с подтверждением
    send_confirmation_email(user)  # Вызов функции отправки письма

    return Response({'success': 'Пользователь зарегистрирован. Проверьте вашу почту для подтверждения.'}, status=status.HTTP_201_CREATED)

# Функция отправки письма
def send_confirmation_email(user):
    subject = 'Подтверждение регистрации'
    message = 'Спасибо за регистрацию! Пожалуйста, подтвердите вашу почту, перейдя по ссылке.'
    from_email = 'your-email@gmail.com'
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)

@login_required
def check_session(request):
    if request.user.is_authenticated:
        return JsonResponse({'authenticated': True}, status=200)
    else:
        return JsonResponse({'authenticated': False}, status=401)

def logout_user(request):
    if request.method == 'POST':  # Обрабатываем только POST запросы для безопасности
        logout(request)  # Выходим из системы
        return JsonResponse({'message': 'Успешный выход'}, status=200)
    return JsonResponse({'error': 'Требуется POST-запрос'}, status=405)