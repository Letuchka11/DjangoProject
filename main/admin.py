from django.contrib import admin
from main.models import Films , Director
# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ['director','title' , 'rating' , 'duration', 'created' , 'updated']
    search_fields = 'title'.split()
    list_filter = ['director','title' , 'rating' , 'duration', 'created' , 'updated']
    list_display_links = None
    list_editable = 'director title rating'.split()

# class DirectorAdmin(admin.ModelAdmin):
    # list_display = ['name']

admin.site.register(Films, FilmAdmin)
admin.site.register(Director )
