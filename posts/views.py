from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import TarotCard
from .serializers import CardSerializer
from .permissions import IsAdminOrReadOnly

import random


class TarotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TarotCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAdminOrReadOnly]


class AllTarotListView(generics.ListAPIView):
    queryset = TarotCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAdminOrReadOnly]


class RandomCardView(GenericAPIView):
    queryset = TarotCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        cards = self.get_queryset()  # Получаем все карты из базы
        if cards.exists():
            random_card = random.choice(cards)  # Случайная карта
            serializer = self.get_serializer(random_card)  # Сериализация карты
            return Response(serializer.data)
        return Response({"detail": "No cards available"}, status=404)


class CardsBySuitView(GenericAPIView):
    queryset = TarotCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, suit, *args, **kwargs):
        # Фильтруем карты по масти
        cards = self.get_queryset().filter(suit=suit)
        if cards.exists():
            serializer = self.get_serializer(cards, many=True)
            return Response(serializer.data)
        return Response({"detail": f"No cards found for suit: {suit}"}, status=404)


class TarotMetaInfoView(APIView):
    """
    Эндпоинт для получения возможных значений мастей и арканов.
    """
    def get(self, request, *args, **kwargs):
        data = {
            "suits": ["Жезлы", "Мечи", "Кубки", "Пентакли"],
        }
        return Response(data)
