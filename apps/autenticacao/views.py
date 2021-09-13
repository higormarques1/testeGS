from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings


def logar(request, template_name="login.html"):
    next = request.GET.get('next', '/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(username=username, password=password)
        except:
            messages.error(request, 'Usuário ou senha incorretos.')
            return redirect('logar')
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return redirect('logar')

    return render(request, template_name, {'redirect_to': next})


@login_required
def deslogar(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)