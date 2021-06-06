from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms

# Create your views here.


def login(request):
    form = forms.LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # ...
            # redirect to a new URL:
            return render(request, 'messenger/login.html')
        else:
            return render(request, 'messenger/login.html')
    else:
        return render(request, 'messenger/login.html',  {'form': form})


def register(request):
    # foo_instance = Foo.objects.create(name='test')
    return render(request, 'messenger/register.html')
