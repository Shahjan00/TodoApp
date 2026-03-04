from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(username, email, password)

        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('/login')
        
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print("login successfully")
            return redirect('/todo')
    return render(request, 'login.html')

@login_required(login_url='/login')
def logout(request):
    auth_logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = Task(title=title, user=request.user)
        obj.save()
    res = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todo.html', {'tasks': res})

@login_required(login_url='/login')
def edit_todo(request,id):
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = Task.objects.get(id=id)
        obj.title = title
        obj.save()
        return redirect('/todo')
    obj = Task.objects.get(id=id)
    return render(request,'edit_todo.html',{'obj':obj})

@login_required(login_url='/login')
def del_todo(request,id):
    # if request.method == 'POST':
        obj = Task.objects.get(id=id)
        obj.delete()
        return redirect('/todo')
