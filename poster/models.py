from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Poster(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posters'
    )
    image = models.ImageField(
        upload_to='posters/%Y/%m/%d/', blank=False
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    tags = TaggableManager()
    users_like = models.ManyToManyField(
        User, related_name='images_liked', blank=True
    )
    total_likes = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['-total_likes'])
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('poster:poster_detail', args=[
            self.id, self.slug
        ])