from django.shortcuts import render

from . import forms

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = forms.LoginForm()
    else:
        return render(request, 'messenger/login.html')


def register(request):
    return render(request, 'messenger/register.html')
