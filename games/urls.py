from django.urls import path

from games.views import verification_mail

urlpatterns = [
    path('verification_mail/', verification_mail, name='verification_mail'),
]
