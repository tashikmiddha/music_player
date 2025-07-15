from django.shortcuts import render, HttpResponse
from .models import songs
import random

def main1(request):
    if "shuffled_songs" not in request.session or not request.session["shuffled_songs"]:
     request.session["shuffled_songs"] = list(songs.objects.values_list("id", flat=True))
     random.shuffle(request.session["shuffled_songs"])

    song_id = request.session["shuffled_songs"].pop(0)
    song = songs.objects.get(id=song_id)
    request.session.modified = True

    if not song:
        return HttpResponse("No songs available")

    s = {
        'title': song.title,
        'artist': song.artist,
        'image': song.image.url , 
        'lyrics': song.lyrics,
        'audio_file': song.audio_file.url , 
        'audio_link': song.audio_link,
        'duration': song.duration,
    }
    return render(request, "main.html", s)


def home(request):
    return render(request,'play.html')
