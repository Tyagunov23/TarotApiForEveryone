
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from posts.views import TarotDetailView, AllTarotListView, RandomCardView, CardsBySuitView, TarotMetaInfoView

urlpatterns = [
    path('tarot/', AllTarotListView.as_view(), name='all-tarot-list'),
    path('tarot/<int:pk>/', TarotDetailView.as_view(), name='tarot-detail'),
    path('tarot/random/', RandomCardView.as_view(), name='random-card'),
    path('tarot/suit/<str:suit>/', CardsBySuitView.as_view(), name='cards-by-suit'),
    path('tarot/meta/', TarotMetaInfoView.as_view(), name='tarot-meta'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
