from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        default='default_profile.jpg', 
        upload_to='profile/%Y/%m/%d/',
        blank=True
    )
    bio = models.CharField(max_length=200, blank=True, default="")

    def __str__(self):
        return f'Profile of {self.user.username}'


    def get_absolute_url(self):
        return reverse('account:profile', args=[
            self.id
        ])