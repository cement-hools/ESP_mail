from django.db import IntegrityError

from esp.interfaces import ESPAbstract
from esp.models import Email


class ProjectESP(ESPAbstract):
    def add_email(self, email: str) -> bool:
        Email.objects.create(email=email)
        return True

    def check_email(self, email: str) -> bool:
        return Email.objects.filter(email=email).exists()
