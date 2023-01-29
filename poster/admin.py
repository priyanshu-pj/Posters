from django.contrib import admin
from .models import Poster

@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'image', 
        'title',
        'slug',
        'created',
        'tags'
    ]
    raw_id_fields = ['user']
    list_filter = [
        'user',
        'created',
        'tags'
    ]
    prepopulated_fields = {'slug': ('title',)}