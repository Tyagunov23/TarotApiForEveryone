from rest_framework import serializers
from django.contrib.auth.models import User


# Сериализатор для карты
class CardSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    number = serializers.CharField(max_length=10)
    arcana = serializers.CharField(max_length=50)
    suit = serializers.CharField(max_length=50, required=False, allow_blank=True)
    description = serializers.CharField()
    image_path = serializers.ImageField(required=False, allow_null=True)

    def create(self, validated_data):
        # Создание объекта модели TarotCard
        from .models import TarotCard
        return TarotCard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Обновление объекта модели TarotCard
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


# Сериализатор для основного объекта
class TarotSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=255)
    cards = CardSerializer(many=True)  # Список объектов карты


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
