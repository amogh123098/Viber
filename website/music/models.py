from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator



class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=550)
    genre = models.CharField(max_length=150)
    album_logo = models.ImageField(upload_to='images', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + '-' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file = models.FileField(upload_to='music', validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'wma'])])
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.album.pk})
