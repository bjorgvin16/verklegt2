from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm

def index(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() #creates the within django

            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}!')

            return redirect('login-index')

    context = {'form' : form}
    return render(request, 'signup/index.html', context)