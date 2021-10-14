from rest_framework import serializers


class EmailValidSerializer(serializers.Serializer):
    """Сериализация email."""
    email = serializers.EmailField()


