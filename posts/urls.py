
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from posts.views import TarotDetailView, AllTarotListView, RandomCardView

urlpatterns = [
    path('tarot/', AllTarotListView.as_view(), name='all-tarot-list'),
    path('tarot/<int:pk>/', TarotDetailView.as_view(), name='tarot-detail'),
    path('tarot/random/', RandomCardView.as_view(), name='random-card'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
