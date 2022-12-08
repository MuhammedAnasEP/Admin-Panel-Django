
from re import search
from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
def admins_log(request):
    if request.user.is_superuser:
        return redirect(admins_home)
    return render(request,'admins_login.html')

@never_cache
def admins_home(request):
    if request.user.is_superuser:
        if 's' in request.POST:
            s = request.POST['s']
            details=User.objects.filter(first_name__icontains=s)
        else:
            details= User.objects.all()
        return render(request,'admins_home.html',{'details':details})
    return redirect(admins_log)
    



def admins_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None and user.is_superuser:
            auth.login(request,user)
            return redirect(admins_home)
        else:
            messages.info(request, 'User Name Not Valid')
            return redirect(admins_log)
    else:
        return render(request,'admins_login.html')

def admins_logout(request):
    if request.user.is_superuser:
        auth.logout(request)
    return redirect('/')


def admins_inse(request):
    return render(request,'admins_insert.html')

def admins_insert(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']   
        last_name=request.POST['last_name']     
        username=request.POST['username']    
        password=request.POST['password1']    
        password2=request.POST['password2']    
        email=request.POST['email'] 


        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'   !! Username Is Taken !! ') 
                return redirect(admins_inse)
            elif User.objects.filter(email=email).exists():
                messages.info(request,'  !! Email is already used !! ')
                return redirect(admins_inse)
            else:
                user= User.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name)
                user.save()
                return redirect(admins_home)
        else:
            messages.info(request,'!! The password are not matching !!')
            return redirect(admins_inse)


def admins_edit(request,id):
    user=User.objects.get(id=id)
    return render(request,'admins_edit.html',{'user_details' : user})


def admins_update(request,id):
    if request.method == 'POST':
         
        user= User.objects.get(id=id)
        first_name=request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')


        user.first_name =  first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()
        return redirect(admins_home)


def admins_delete(request,id):
    user_del=User.objects.get(id=id)
    user_del.delete()
    user = User.objects.all()
    return redirect(admins_home)
