from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from account.models import Profile

@login_required
def dashboard(request):
    # return HttpResponse('Home')
    return render(request, 'home/dashboard.html')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print('fetched data')
            new_user =  form.save(commit=False)
            print('created user')
            new_user.set_password(cd['password'])
            new_user.save()
            print('saved user')
            # Automatically create Profile object for the user
            Profile.objects.create(user=new_user)
            return render(request, 'home/registered.html', {'new_user': new_user})
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = UserRegistrationForm()
    return render(request, 'home/register.html', {'form': form})