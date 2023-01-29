from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileEditForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile


@login_required
def edit(request):
    user = request.user
    if request.method == "POST":
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST,
        )
        try:
            if profile_form.is_valid() and user_form.is_valid():
                profile_form.save()
                user_form.save()
        except:
            return HttpResponse('Please enter more comman image type')
            
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
        user_form = UserEditForm(instance=request.user)
    return render(request, 'account/edit.html', {
        'profile_form': profile_form, 
        'user_form': user_form,
        'user': user
    })


@login_required
def profile(request, id):
    profile = get_object_or_404(
        Profile,
        id=id
    )
    posters = profile.user.posters.all()
    return render(request, 'account/profile.html', {
        'profile': profile,
        'posters': posters
    })