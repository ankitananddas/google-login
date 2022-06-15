from django.shortcuts import render, redirect
from .models import Profile, Task
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def Home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    task = Task.objects.all()
    return render(request, 'base/home.html', {
        "task": task
    })


def Add_task(request):
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        title = request.POST['title']
        description = request.POST['descrip']
        add = Task.objects.create(user=user, title=title, descrip=description)
        if add:
            messages.success(request, "Task Added")
            return redirect(request, 'home')
    return render(request, 'base/add_task.html')


def removeTask(request):
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)

        if remove:
            messages.success(request, "Task Deleted")
            return redirect(request, 'home')
    return render(request, 'base/remove.html')


def Login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
    return render(request, 'base/Login.html')


def Logout(request):
    logout(request)
    return redirect("login")
