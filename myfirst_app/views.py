from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from myfirst_app.forms import User,User_info_form

def index(request):
    #mydict={'insert_me':"Thala takkar "}
    return render(request,'myfirst_app\index.html')
def formcv(request):
    form=forms.cv()
    if request.method=="POST":
        form=forms.cv(request.POST)
        if form.is_valid():
            print('Its successful submission ')
            print("Name"+form.cleaned_data['name'])
    return render(request,'myfirst_app/forms.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,'myfirst_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))





def register(request):
    registered=False
    if request.method=="POST":
        user=User(request.POST)
        user_prof=User_info_form(request.POST)
        if user.is_valid() and user_prof.is_valid():
            usero=user.save()
            usero.set_password(usero.password)
            usero.save()
            user_profo=user_prof.save(commit=False)
            user_profo.user=usero
            if 'profile_pic' in request.FILES:
                user_profo.profile_pic=request.FILES['profile_pic']
            user_profo.save()
            registered=True
            HttpResponseRedirect(reverse('index'))
        else:
            print(user.errors,user_prof.errors)
    else:
        user=User()
        user_prof=User_info_form()
        return render(request,'myfirst_app/register.html',{'user':user,'user_prof':user_prof})





# Create your views here.
