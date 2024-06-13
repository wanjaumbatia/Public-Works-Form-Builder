from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authentication.forms import RegistrationForm

def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid username or password.', 'username': request.POST['username']})
        
    return render(request, 'auth/login.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})


@login_required()
def log_out(request):
    logout(request)
    return redirect('/login')
