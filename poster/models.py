from django.db import models
from taggit.managers import TaggableManager


class Poster(models.Model):
    image = models.ImageField(
        upload_to='posters/%Y/%m/%d/', blank=False
    )
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    tags = TaggableManager()