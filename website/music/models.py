from django.db import models

class Artist(models.Model):
    artist_id = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=400)
    description = models.TextField()
    origin_url = models.CharField(max_length=400)

class Song(models.Model):
    song_id = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artist, related_name="songs")
    lyric = models.TextField()
    cover_img_url = models.CharField(max_length=400)
    origin_url = models.CharField(max_length=400)
