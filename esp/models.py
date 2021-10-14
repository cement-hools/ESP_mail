from django.db import models


class Email(models.Model):
    email = models.EmailField('Email пользователя')

    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'emails'
