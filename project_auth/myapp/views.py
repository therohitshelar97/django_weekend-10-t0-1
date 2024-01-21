from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Appointment
from django.contrib import messages

# Create your views here.
def Index(request):
    return render(request,'index.html')

def SignUp(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass')
        User.objects.create_user(uname,email,pass1)
    return render(request,'signup.html')

def Login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/appoint/')
    else:
        if request.method == "POST":
            uname = request.POST.get('uname')
            pass1 = request.POST.get('pass')
            user = authenticate(request,username=uname,password=pass1)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/appoint/')
            else:
                return HttpResponseRedirect('/signup/')
        return render(request,'login.html')

def Appointment1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            contact = request.POST.get('cnumber')
            what = request.POST.get('what')
            Appointment.objects.create(name=name,contact=contact,reason=what,user=request.user)
            messages.success(request,"We Got Data Will Confirm You Appointment Time...")
        data = Appointment.objects.filter(user_id=request.user)
        return render(request,'appointment.html',{'data':data})
    else:
        return HttpResponseRedirect('/login/')
    
def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/login/')


