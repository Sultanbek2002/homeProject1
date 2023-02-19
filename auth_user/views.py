from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            redirect('login')
    return render(request, 'auth_user/login.html')


def logout(request):
    print("dsafmkjhdchdjkahsfhdiumnjhfncjkdhiah",request)
    auth.logout(request)
    redirect('home')
