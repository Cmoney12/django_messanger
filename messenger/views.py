from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = forms.LoginForm()
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        else:
            return render(request, 'messenger/login.html')
    else:
        return render(request, 'messenger/login.html')


def register(request):
    return render(request, 'messenger/register.html')
