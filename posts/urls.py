
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from posts.views import TarotListCreateView, TarotDetailView, AllTarotListView

urlpatterns = [
    path('tarot/', TarotListCreateView.as_view(), name='tarot-list-create'),
    path('tarot/<int:pk>/', TarotDetailView.as_view(), name='tarot-detail'),
    path('tarot/all/', AllTarotListView.as_view(), name='all-tarot-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
