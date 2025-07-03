from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Case, When, Value, IntegerField
from .models import Artist, Song
import time

page_max_lines = 10

def mainpage(request):
    return render(request, 'music/mainpage.html')

def song_list(request):
    songs_all = Song.objects.all().order_by('id')
    paginator = Paginator(songs_all, page_max_lines)
    page_number = request.GET.get('page')
    songs = paginator.get_page(page_number)
    return render(request, 'music/song_list.html', {'songs': songs})


def song_detail(request, id):
    song = get_object_or_404(Song, song_id=id)
    artists = song.artist.all()
    return render(request, 'music/song_detail.html', {'song': song, 'artists': artists})


def artist_list(request):
    artists_all = Artist.objects.all().order_by('id')
    paginator = Paginator(artists_all, page_max_lines)
    page_number = request.GET.get('page')
    artists = paginator.get_page(page_number)
    return render(request, 'music/artist_list.html', {'artists': artists})


def artist_detail(request, id):
    artist = get_object_or_404(Artist, artist_id=id)
    songs_all = Song.objects.filter(artist__artist_id=id)
    paginator = Paginator(songs_all, page_max_lines)
    page_number = request.GET.get('page')
    songs = paginator.get_page(page_number)
    return render(request, 'music/artist_detail.html', {'artist': artist, 'songs': songs})

def search(request):
    query = request.GET.get('q', '')
    search_type = request.GET.get('type', 'song')
    page_number = request.GET.get('page')

    start_time = time.time()

    if search_type == 'song':
        # 按名称、艺术家、歌词的优先级展示搜索结果
        name_match = Q(name__icontains=query)
        artist_match = Q(artist__name__icontains=query)
        lyric_match = Q(lyric__icontains=query)
        results_all = Song.objects.filter(
            name_match | 
            artist_match | 
            lyric_match
        ).annotate(
            match_priority=Case(
                When(name_match, then=Value(1)),
                When(artist_match, then=Value(2)),
                When(lyric_match, then=Value(3)),
                default=Value(4),
                output_field=IntegerField()
            )
        ).order_by('match_priority', 'name').distinct()

    elif search_type == 'artist':
        name_match = Q(name__icontains=query)
        description_match = Q(description__icontains=query)
        results_all = Artist.objects.filter(
            name_match | 
            description_match
        ).annotate(
            match_priority=Case(
                When(name_match, then=Value(1)),
                When(description_match, then=Value(2)),
                default=Value(3),
                output_field=IntegerField()
            )
        ).order_by('match_priority', 'name').distinct()
    
    paginator = Paginator(results_all, page_max_lines)
    # 传入参数, 便于翻页时保持其他参数
    query_params = request.GET.copy()
    if 'page' in query_params:
        del query_params['page']
    results = paginator.get_page(page_number)

    search_time = round(time.time() - start_time, 2)
    search_count = results_all.count()

    return render(request, 'search_result.html', {
        'query': query,
        'search_type': search_type,
        'results': results,
        'query_params': query_params,
        'search_count': search_count,
        'search_time': search_time
    })