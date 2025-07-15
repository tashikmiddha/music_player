from django.db import models

class songs(models.Model):  
    title = models.TextField()
    artist = models.TextField()
    image = models.ImageField(upload_to="song_images/", blank=True, null=True)  
    audio_file = models.FileField(upload_to="song_audio/") 
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True) 
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.title
