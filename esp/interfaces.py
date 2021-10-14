from abc import ABC, abstractmethod


class ESPAbstract(ABC):
    """."""

    @abstractmethod
    def check_email(self, email: str) -> bool:
        """"Есть ли email в списке рассылки."""
        pass

    @abstractmethod
    def add_email(self, email: str) -> bool:
        """"Есть ли email в списке рассылки."""
        pass
