from django.db import models


class TarotCard(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    arcana = models.CharField(max_length=50)
    suit = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    image_path = models.ImageField(upload_to='tarotcards/', null=True, blank=True)  # Путь к изображению карты

    def __str__(self):
        return f"{self.name} ({self.arcana})"
