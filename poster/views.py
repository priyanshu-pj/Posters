from django.shortcuts import render
from .models import Poster
from django.contrib.auth.decorators import login_required
from .forms import PosterCreationForm


@login_required
def explore(request):
    posters = Poster.objects.all()
    return render(request, 'poster/explore.html', {'posters': posters})


@login_required
def create_poster(request):
    poster_creation_form = PosterCreationForm()
    return render(request, 'poster/create_poster.html', {
        'poster_creation_form': poster_creation_form
    })