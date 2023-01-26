from django.shortcuts import render, get_object_or_404
from .models import Poster
from django.contrib.auth.decorators import login_required
from .forms import PosterCreationForm


@login_required
def explore(request):
    posters = Poster.objects.all()
    return render(request, 'poster/explore.html', {'posters': posters})


@login_required
def create_poster(request):
    if request.method == "POST":
        poster_creation_form = PosterCreationForm(request.POST)
        if poster_creation_form.is_valid():
            cd = poster_creation_form.cleaned_data
            if cd['user'] == request.user:
                print('\n\n\nUser error\n\n\n')
                poster_creation_form.save()
            else:
                poster_creation_form.user = request.user
    return render(request, 'poster/create_poster.html', {
        'poster_creation_form': poster_creation_form
    })


def poster_detail(self, id, slug):
    try:
        poster = get_object_or_404(
            Poste, id=id, slug=slug
        )
        return render(request, 'poster/poster_detail.html', {'poster': poster})
    except Poster.DoesNotExist:
        return redirect('home/dashboard.html')