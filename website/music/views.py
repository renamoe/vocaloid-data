from django.shortcuts import render, get_object_or_404
from .models import Artist, Song

def mainpage(request):
    return render(request, 'music/mainpage.html')

def song_list(request):
    songs = Song.objects.all().order_by('name')
    return render(request, 'music/song_list.html', {'songs': songs})


def song_detail(request, id):
    song = get_object_or_404(Song, song_id=id)
    artists = song.artist.all()
    return render(request, 'music/song_detail.html', {'song': song, 'artists': artists})


def artist_list(request):
    artists = Artist.objects.all().order_by('name')
    return render(request, 'music/artist_list.html', {'artists': artists})


def artist_detail(request, id):
    artist = get_object_or_404(Artist, artist_id=id)
    songs = Song.objects.filter(artist__artist_id=id)
    return render(request, 'music/artist_detail.html', {'artist': artist, 'songs': songs})