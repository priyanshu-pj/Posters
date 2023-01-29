from django.shortcuts import render, get_object_or_404
from .models import Poster
from django.contrib.auth.decorators import login_required
from .forms import PosterCreationForm
from django.http import HttpResponse


@login_required
def poster_list(request):
    posters = Poster.objects.all()
    return render(request, 'poster/poster_list.html', {'posters': posters})


@login_required
def poster_detail(request, id, slug):
    poster = get_object_or_404(
        Poster,
        id=id, slug=slug
    )
    return render(request, 'poster/poster_detail.html', {'poster': poster})