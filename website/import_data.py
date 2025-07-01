import os
import json
import django
from tqdm import tqdm

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from music.models import Song, Artist

def import_artists(json_file):
    """ 将 json 文件中的艺术家信息导入 django 数据库
    Args:
        json_file(str): 艺术家信息 json 文件路径
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for id, artist in tqdm(data.items(), desc='导入艺术家信息'):
        Artist.objects.create(
            artist_id=id,
            name=artist['name'],
            img_url=artist['img_url'],
            description=artist['description'],
            origin_url=artist['origin_url']
        )

def import_songs(json_file: str):
    """ 将 json 文件中的歌曲信息导入 django 数据库
    Args:
        json_file(str): 歌曲信息 json 文件路径
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for id, song in tqdm(data.items(), desc='导入歌曲信息'):
        song_obj = Song.objects.create(
            song_id=id,
            name=song['name'],
            lyric=song['lyric'],
            cover_img_url=song['cover_img_url'],
            origin_url=song['origin_url']
        )
        artist_ids = [x['id'] for x in song['artist']]
        artists = Artist.objects.filter(artist_id__in=artist_ids)
        song_obj.artist.set(artists)


import_artists('../data/artist_info.json')
import_songs('../data/song_info.json')
