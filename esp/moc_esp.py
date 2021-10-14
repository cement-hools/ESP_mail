from typing import List

from esp.interfaces import ESPAbstract
from esp.models import Email


class ProjectESP(ESPAbstract):
    def add_email(self, email: str) -> bool:
        """"Добавить email в список рассылки."""
        Email.objects.create(email=email)
        return True

    def check_email(self, email: str) -> bool:
        """"Наличие email в списке рассылки."""
        return Email.objects.filter(email=email).exists()

    def add_email_list(self, email_list: List[str]) -> bool:
        """"Добавить несколько email в список рассылки."""
        pass

    def del_email(self, email: str) -> bool:
        """"Удалить email из списка рассылки."""
        pass

    def del_email_list(self, email_list: List[str]) -> bool:
        """"Удалить список email из списка рассылки."""
        pass

    def send_all(self, text):
        """Отправить сообщение всем адресам из списка."""
        pass


