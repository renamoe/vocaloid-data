from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.song_list, name="mainpage"),
    path('songs/', views.song_list, name="song_list"),
    path('songs/<str:id>', views.song_detail, name="song_detail"),
    path('artists/', views.artist_list, name="artist_list"),
    path('artists/<str:id>', views.artist_detail, name="artist_detail"),
    path('search/', views.search, name='search')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)