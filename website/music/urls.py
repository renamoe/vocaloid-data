from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('songs/', views.song_list, name="song_list"),
    path('songs/<str:id>', views.song_detail, name="song_detail"),
    path('artists/', views.artist_list, name="artist_list"),
    path('artists/<str:id>', views.artist_detail, name="artist_detail"),
]