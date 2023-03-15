from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            redirect('login')
    return render(request, 'auth_user/login.html')


def logout(request):
    print("dsafmkjhdchdjkahsfhdiumnjhfncjkdhiah", request)
    auth.logout(request)
    redirect('home')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        again_password = request.POST['again_password']
        if password == again_password:
            if User.objects.filter(username == username).exists():
                return redirect('login')
            else:
                if User.objects.filter(email == email).exists():
                    return redirect('login')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    auth.login(request, user)
                    return redirect('home')
        else:
            return redirect('register')
    else:
        return render(request, 'auth_user/register.html')


def profile(request):
    return render(request, 'auth_user/profile.html')
