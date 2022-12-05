from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid user')
            return redirect('login')
    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email_id = request.POST['email_id']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                email=email_id, password=password)
                user.save();
                return redirect('login')
                print('USER CREATED')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, 'register.html')

