from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # return HttpResponse('Home')
    return render(request, 'home/dashboard.html')