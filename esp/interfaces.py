from abc import ABC, abstractmethod
from typing import List


class ESPAbstract(ABC):
    """Абстрактный класс ESP."""

    @abstractmethod
    def check_email(self, email: str) -> bool:
        """"Наличие email в списке рассылки."""
        pass

    @abstractmethod
    def add_email(self, email: str) -> bool:
        """"Добавить email в список рассылки."""
        pass

    @abstractmethod
    def add_email_list(self, email_list: List[str]) -> bool:
        """"Добавить несколько email в список рассылки."""
        pass

    @abstractmethod
    def del_email(self, email: str) -> bool:
        """"Удалить email из списка рассылки."""
        pass

    @abstractmethod
    def del_email_list(self, email_list: List[str]) -> bool:
        """"Удалить список email из списка рассылки."""
        pass

    @abstractmethod
    def send_all(self, text):
        """Отправить сообщение всем адресам из списка."""
        pass


