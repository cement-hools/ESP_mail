from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from esp.moc_esp import ProjectESP
from games.models import Game
from games.serializers import EmailValidSerializer

ESP = ProjectESP()


@api_view(['POST'])
def verification_mail(request, *args, **kwargs):
    """
    Получения email из запроса
    Проверка валидности
    Добавление email в ESP если он отсутствует в списке
    Создание записи об игре
    Вывод количество игр для email.
    """
    serializer = EmailValidSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    email = serializer.data.get('email')
    email_in_esp = ESP.check_email(email=email)

    games_count = Game.objects.filter(email=email).count()

    response = {
        'esp_status': email_in_esp,
        'games_status': False,
        'games_count': games_count,
    }

    if games_count > 0:
        response['games_status'] = True
        return Response(response, 201)

    if not email_in_esp:
        ESP.add_email(email=email)
    Game.objects.create(email=email)
    response['games_count'] += 1

    return Response(response, 201)

