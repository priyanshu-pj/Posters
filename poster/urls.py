from django.urls import path
from . import views

app_name = "poster"

urlpatterns = [
    path('explore/', views.explore, name='explore'),
    path('create-new-poster/', views.create_poster, name='create_poster'),
]