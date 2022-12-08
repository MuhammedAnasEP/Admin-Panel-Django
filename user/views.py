from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from home.views import home
from django.views.decorators.cache import never_cache

# Create your views here.
def user_register(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email is already used')
                return redirect('user_register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('/')
        else:
            messages.info(request,'The password is not matching!')
            return redirect('user_register')
        return redirect('/')
    else:
      return render (request,'user_register.html')
@never_cache
def user_login(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            messages.info(request, 'invalid credentials')
            return redirect('user_login')
    else:
        return render(request,"user_login.html")
@never_cache
def user_logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')