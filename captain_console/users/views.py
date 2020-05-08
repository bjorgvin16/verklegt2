from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'userprofile/index.html')


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() #creates the within django

            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}!')

            return redirect('users-login')

    context = {'form' : form}
    return render(request, 'signup/index.html', context)

# Fallið hennar Möggu

''' def loginUser(request):

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
    return render(request, 'login/index.html', context) '''

def logoutUser(request):
	logout(request)
	return render(request,'frontpage/index.html')
