from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

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

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('frontpage-index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login/index.html", context={"form":form})

def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out successfully!")

    return redirect("frontpage-index")
