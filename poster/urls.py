from django.urls import path
from . import views

app_name = "poster"

urlpatterns = [
    path('poster-list/', views.poster_list, name='poster_list'),
    path('poster-detail/<int:id>/<slug:slug>/', views.poster_detail, name='poster_detail'),
]