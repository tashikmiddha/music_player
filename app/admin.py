from django.contrib import admin
from .models import songs

# admin.site.register(songs)
@admin.register(songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "duration")  # Display these fields in the list view
    search_fields = ("title", "artist")  # Enable search by title and artist
    list_filter = ("artist",)  # Add a filter sidebar for artists