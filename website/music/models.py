from django.db import models

class Artist(models.Model):
    artist_id = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=400)
    description = models.TextField()
    origin_url = models.CharField(max_length=400)
    
    @property
    def get_img_path(self):
        if len(self.img_url) == 0:
            return '/media/img_artist/default.jpg'
        return '/media/img_artist/' + self.artist_id + '.jpg'
    
    @property
    def get_detail_page(self):
        return '/artists/' + self.artist_id

class Song(models.Model):
    song_id = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artist, related_name="songs")
    lyric = models.TextField()
    cover_img_url = models.CharField(max_length=400)
    origin_url = models.CharField(max_length=400)

    @property
    def get_img_path(self):
        return '/media/img_song_cover/' + self.song_id + '.jpg'
    
    @property
    def get_detail_page(self):
        return '/songs/' + self.song_id
