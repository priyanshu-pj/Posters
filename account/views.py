from django.shortcuts import render
from .forms import ProfileEditForm, UserEditForm
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    profile_form = ProfileEditForm()
    user_form = UserEditForm()
    user = request.user
    return render(request, 'account/profile.html', {
        'profile_form': profile_form, 
        'user_form': user_form,
        'user': user
    })