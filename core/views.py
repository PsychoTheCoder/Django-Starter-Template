from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, "core/index.html")


def handleLogin(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data["username"], password=data["password"])
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect("homepage")
        else:
            messages.error(request, "Error! Make sure your credientials are correct & Try Again")

    return render(request, "core/login.html")


def handleSignup(request):
    if request.method == "POST":
        data = request.POST
        print(data["username"])
        if User.objects.filter(username=data["username"]).exists():
            messages.info(request, 'Username is already taken please choose different')
            return redirect("signup")
        elif User.objects.filter(email=data["email"]).exists():
            messages.info(request, 'Email is already taken')
            return redirect("signup")
        else:
            newUser = User.objects.create_user(data["username"], data["email"], data["password"])
            newUser.save()
            messages.success(request, "Account Created Successfully. You can login now.")
            return redirect("homepage")

    return render(request, "core/signup.html")

def handlelogout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Account Logout Success")
        return redirect("homepage")