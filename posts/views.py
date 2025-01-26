from rest_framework import generics

from .models import TarotCard
from .serializers import CardSerializer
from .permissions import IsAuthorOrReadOnly


class TarotListCreateView(generics.ListCreateAPIView):
    queryset = TarotCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthorOrReadOnly]


class TarotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TarotCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthorOrReadOnly]


class AllTarotListView(generics.ListAPIView):
    queryset = TarotCard.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthorOrReadOnly]
