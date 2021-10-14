from django.db import models


class Game(models.Model):
    email = models.EmailField('Email пользователя')
    created = models.DateTimeField('Дата и время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'game'
        verbose_name_plural = 'games'

