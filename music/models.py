
from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    def __str__(self):
        return self.artist_name
    
class Genra(models.Model):
    genra_name = models.CharField(max_length=200)
    def __str__(self):
        return self.genra_name

class Album(models.Model):
    album_name = models.CharField(max_length=200)
    album_genra = models.ForeignKey(Genra, default=4, on_delete=models.CASCADE)
    album_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_release_year = models.IntegerField(default=0)
    def __str__(self):
        return self.album_name

class Song(models.Model):
    song_name = models.CharField(max_length=200)
    song_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.song_name

