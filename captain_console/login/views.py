from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


def index(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('frontpage-index')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login/index.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login/index.html')
